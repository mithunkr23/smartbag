import cv2
import pandas as pd
import datetime
from twilio.rest import Client

# -------------------------------
# Student Info
# -------------------------------
student_name = "Mithun"   # Change this if needed

# -------------------------------
# Embedded Book Data (QR codes)
# -------------------------------
books_data = [
    {"Subject": "CN", "Book Name": "Computer notes", "QR ID": "CN001"},
    {"Subject": "SE", "Book Name": "Software Engineering", "QR ID": "SE001"},
    {"Subject": "DS", "Book Name": "Distributed Systems", "QR ID": "DS001"}
]
books_df = pd.DataFrame(books_data)

# -------------------------------
# Embedded Timetable Data
# -------------------------------
timetable_data = [
    {"Day": "Monday", "Subject": "CN"},
    {"Day": "Monday", "Subject": "SE"},
    {"Day": "Tuesday", "Subject": "DS"},
    {"Day": "Tuesday", "Subject": "CN"},
    {"Day": "Wednesday", "Subject": "SE"},
    {"Day": "Wednesday", "Subject": "CN"},
    {"Day": "Wednesday", "Subject": "DS"},
    {"Day": "Thursday", "Subject": "CN"},
    {"Day": "Thursday", "Subject": "SE"},
    {"Day": "Friday", "Subject": "DS"},
    {"Day": "Friday", "Subject": "CN"},
    {"Day": "Sunday", "Subject": "SE"},
    {"Day": "Saturday", "Subject": "DS"}
]
timetable_df = pd.DataFrame(timetable_data)

# -------------------------------
# Twilio SMS Setup
# -------------------------------
account_sid = 'AC9e1559c8ccaf6ae4d459f6f9528382a9'   # Replace with your Twilio SID
auth_token = '62d924dd3afa9d611b41da82c4f6fd45'     # Replace with your Twilio Auth Token
twilio_number = '+18584282410'                      # Replace with your Twilio phone number
my_number = '+918050708166'                         # Replace with your phone number
client = Client(account_sid, auth_token)

# -------------------------------
# Function: Scan Books via Webcam (Optimized QR only)
# -------------------------------
def scan_books(duration=15, expected_subjects=None):
    detected_books = []
    cap = cv2.VideoCapture(0)
    qr_detector = cv2.QRCodeDetector()
    start_time = datetime.datetime.now()
    frame_count = 0

    while (datetime.datetime.now() - start_time).seconds < duration:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (640, 480))
        frame_count += 1
        if frame_count % 3 != 0:  # process every 3rd frame
            continue

        retval, decoded_info, points, _ = qr_detector.detectAndDecodeMulti(frame)

        if retval:
            for i, qr_data in enumerate(decoded_info):
                qr_data = qr_data.strip()
                if qr_data and qr_data not in detected_books:
                    detected_books.append(qr_data)
                    print("✅ Detected QR ID:", qr_data)

                if points is not None:
                    pts = points[i].astype(int).reshape((-1, 1, 2))
                    frame = cv2.polylines(frame, [pts], True, (0, 255, 0), 2)

        cv2.imshow("Smart Bag Camera (Optimized)", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Stop scanning as soon as all expected books are found
        if expected_subjects:
            detected_subjects = books_df[books_df['QR ID'].isin(detected_books)]['Subject'].tolist()
            if all(sub in detected_subjects for sub in expected_subjects):
                print("📚 All required books detected. Stopping early.")
                break

    cap.release()
    cv2.destroyAllWindows()
    return detected_books

# -------------------------------
# Function: Check Books + Send SMS
# -------------------------------
def check_books():
    today_day = datetime.datetime.today().strftime('%A')
    today_subjects = timetable_df[timetable_df['Day'] == today_day]['Subject'].tolist()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")

    print(f"\n📅 Today is {today_day}. Required subjects: {today_subjects}")

    detected_books = scan_books(duration=30, expected_subjects=today_subjects)
    
    detected_subjects = books_df[books_df['QR ID'].isin(detected_books)]['Subject'].tolist()
    missing_books = [sub for sub in today_subjects if sub not in detected_subjects]
    
    print("\n✅ Detected Books:", detected_subjects if detected_subjects else "None")
    print("❌ Missing Books:", missing_books if missing_books else "No Missing Books")
    
    # -------------------------------
    # Send SMS depending on result
    # -------------------------------
    if not missing_books:
        sms_text = (
            f"📢 Smart Bag Alert for {student_name}\n"
            f"📅 {today_day} ({timestamp})\n"
            f"✅ All required books are present: {', '.join(today_subjects)}"
        )
    else:
        sms_text = (
            f"⚠️ Smart Bag Alert for {student_name}\n"
            f"📅 {today_day} ({timestamp})\n"
            f"❌ Missing books: {', '.join(missing_books)}\n"
            f"✅ Detected: {', '.join(detected_subjects) if detected_subjects else 'None'}"
        )

    message = client.messages.create(
        body=sms_text,
        from_=twilio_number,
        to=my_number
    )
    print("📩 SMS sent:\n", sms_text)

# -------------------------------
# Run check
# -------------------------------
check_books()