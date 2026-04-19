# Smart Bag System using Computer Vision and QR Detection

An intelligent automation system designed to assist students in organizing their daily academic materials. This project uses computer vision and QR code detection to verify whether the required books are present in a bag based on a predefined timetable, and sends real-time SMS alerts if any items are missing.

---

## Demo

### Working Video

[Watch Demo Video](https://drive.google.com/file/d/1ddBcKSZDs31Y3VBPD1wH4PEnru0fO8hI/view?usp=drivesdk)

### Screenshots

![Book Detection](https://drive.google.com/file/d/1dfuQFfhFfasJq9KZD0u7-t25qHawMWca/view?usp=drivesdk)
![Detected Book](https://drive.google.com/file/d/1jyuBIGwlGm6ycSjRtenbDLQM6kKc2vmr/view?usp=drivesdk)
![SMS alert on Mobile](https://drive.google.com/file/d/1qoP69UzDnh-FyRBKpXOIY3D_RQu6ppyR/view?usp=drivesdk)

---

## Problem Statement

Students often forget to carry the correct books according to their daily schedule. This leads to inconvenience and reduced productivity. There is a need for a smart system that can automatically verify and notify users about missing study materials.

---

## Solution

The Smart Bag System uses a webcam to scan QR codes attached to books. It compares detected books with the subjects scheduled for the day and instantly alerts the user via SMS if any required books are missing.

---

## Key Features

* Real-time QR code detection using computer vision
* Automatic verification of books based on timetable
* Intelligent identification of missing items
* SMS alerts for instant notification
* Optimized scanning for faster performance
* Simple and scalable architecture

---

## System Architecture

1. Input: Webcam captures real-time video
2. Processing: QR code detection using OpenCV
3. Data Handling: Book and timetable data managed using Pandas
4. Logic Layer: Comparison of detected books with required subjects
5. Output: SMS notification via Twilio API

---

## Technologies Used

* Python
* OpenCV
* Pandas
* Twilio API
* Webcam Integration

---

## Installation and Setup

### Install Dependencies

```bash
pip install opencv-python pandas twilio
```

### Configure Credentials

Update the following fields in the code:

* Twilio Account SID
* Twilio Auth Token
* Twilio Phone Number
* Receiver Phone Number

---

## Execution

```bash
python smart_bag.py
```

---

## Workflow

* The system identifies the current day
* Fetches required subjects from the timetable
* Scans QR codes from books using the webcam
* Maps detected QR IDs to subjects
* Compares detected and required subjects
* Sends an SMS alert with results

---

## Sample Output

Today is Monday. Required subjects: CN, SE
Detected Books: CN
Missing Books: SE
SMS sent successfully

---

## Applications

* Smart school bag systems
* Educational automation solutions
* IoT-based student assistance tools
* AI-enabled daily task verification systems

---

## Limitations

* Requires QR codes on all books
* Dependent on camera quality and lighting
* Static dataset (no dynamic updates)
* Requires internet for SMS functionality

---

## Future Enhancements

* Mobile application integration
* Cloud-based database for dynamic timetable updates
* Voice assistant integration
* AI-based object detection without QR codes
* Real-time dashboard for monitoring

---

## Conclusion

This project demonstrates how computer vision and automation can be applied to solve everyday problems. The Smart Bag System is a scalable and practical solution that can be further extended into a full-fledged smart educational assistant.

---

## Author

Mithun K R
