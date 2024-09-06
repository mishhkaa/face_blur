# Face Blur Application

This project is a simple **OpenCV-based Python application** that detects faces in real-time from your webcam and applies a blur effect to the detected faces. It uses a pre-trained Haar Cascade classifier to detect faces and then applies **Gaussian blur** to anonymize them.

## Features:
- Real-time face detection from a webcam.
- Blurs faces in the captured video stream for privacy.
- Uses OpenCV's **Haar Cascade** for face detection.
- Simple and fast processing with a user-friendly interface.

## How It Works:
1. The application captures video input from the default webcam using OpenCV.
2. It converts each frame to grayscale for more efficient face detection.
3. The Haar Cascade classifier is used to detect faces in each frame.
4. Once faces are detected, a Gaussian blur is applied to each face region.
5. The frame with blurred faces is displayed in a window in real-time.

## Dependencies:
- **Python 3.x**
- **OpenCV** (cv2)

