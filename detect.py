import cv2
import pyttsx3
import time
import re
from ultralytics import YOLO

# 1. Initialize the Voice Engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech

# 2. Load Your Custom AI Brain
# Make sure best.pt is in the same folder as this script!
model = YOLO('best.pt')

# 3. Start the Webcam
cap = cv2.VideoCapture(0)

# Timers so it doesn't talk over itself
last_spoken = ""
last_spoken_time = 0
cooldown_seconds = 4

print("Camera starting... Hold up a Rupee note! Press 'q' to quit.")

while True:
    success, frame = cap.read()
    if not success:
        break

    # Run the AI on the current frame (only trust it if it's 70% sure)
    results = model(frame, stream=True, conf=0.70)

    for result in results:
        boxes = result.boxes
        for box in boxes:
            # Get the raw class name (e.g., "6- 500 Rupees")
            class_id = int(box.cls[0])
            raw_name = model.names[class_id]

            # Clean up the name for speech (Removes the "6-" part)
            clean_name = re.sub(r'^\d+-\s*', '', raw_name)

            # Draw a box on the screen
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, clean_name, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

            # Speak out loud if it's a new note or the cooldown has passed
            current_time = time.time()
            if (clean_name != last_spoken) or (current_time - last_spoken_time > cooldown_seconds):
                print(f"Detected: {clean_name}")
                engine.say(clean_name)
                engine.runAndWait()

                last_spoken = clean_name
                last_spoken_time = current_time

    # Show the video feed
    cv2.imshow("Indian Currency Assistant", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
