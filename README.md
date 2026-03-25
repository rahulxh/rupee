# 🇮🇳 Indian Currency Detection AI

A real-time Computer Vision application that uses a custom-trained YOLOv8 neural network to detect and identify Indian Rupee notes through a live webcam feed. Includes integrated Text-to-Speech (TTS) for audio feedback.

## ✨ Features
* **Real-Time Detection:** Processes live video to identify currency denominations (₹10, ₹20, ₹50, ₹100, ₹200, ₹500, ₹2000).
* **High Accuracy:** Custom-trained YOLOv8 model achieving a 0.95 mAP50.
* **Audio Feedback:** Uses `pyttsx3` to speak the detected currency value out loud.
* **Automated Logging:** Saves a text-based receipt of all scanned notes.

## 🛠️ Tech Stack
* **Python 3**
* **Ultralytics YOLOv8** (Object Detection)
* **OpenCV** (Webcam & Image Processing)
* **Pyttsx3** (Text-to-Speech)

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/rahulxh/rupee.git](https://github.com/rahulxh/rupee.git)
   cd rupee
