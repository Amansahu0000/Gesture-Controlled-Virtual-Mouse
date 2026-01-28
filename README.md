# Gesture-Controlled-Virtual-Mouse
This project implements a Gesture-Controlled Virtual Mouse using computer vision techniques, where hand gestures captured through a webcam are used to control mouse movements and click actions in real time, enabling touch-free and intuitive human–computer interaction.

Gesture-Controlled Virtual Mouse 🖱️

This project implements a **Gesture-Controlled Virtual Mouse** using **AI-inspired Computer Vision techniques**. It allows users to control mouse movements and click actions using hand gestures captured through a webcam, eliminating the need for a physical mouse.

---

## 📌 Project Overview

Traditional mouse devices require physical interaction and may not be suitable for touchless environments. This project provides a real-time, contactless solution by detecting hand gestures and mapping them to mouse operations such as cursor movement and clicking.

---

## ⚙️ Technologies Used

- Python
- OpenCV
- NumPy
- PyAutoGUI
- Webcam (for real-time input)
- Visual Studio Code (development environment)

---

## 🧠 System Approach

- Captures real-time video using a webcam
- Converts frames to HSV color space
- Detects skin regions using thresholding
- Identifies hand contour and fingertip position
- Maps fingertip movement to screen coordinates
- Performs mouse actions using PyAutoGUI

---

## ▶️ How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/your-username/Gesture-Controlled-Virtual-Mouse.git
