import cv2

print("Scanning for attached USB webcams...")
print("Please wait, checking drivers...\n")

working_index = None
working_backend = None

for i in range(4):  # Check ports 0, 1, 2, and 3
    print(f"Testing port {i}...")

    # Test 1: Standard Windows Connection
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"✅ SUCCESS! USB Camera found at index: {i} (Standard)")
        working_index = i
        cap.release()
        break

    # Test 2: Windows Media Foundation (MSMF)
    cap = cv2.VideoCapture(i, cv2.CAP_MSMF)
    if cap.isOpened():
        print(f"✅ SUCCESS! USB Camera found at index: {i} (MSMF)")
        working_index = i
        working_backend = cv2.CAP_MSMF
        cap.release()
        break

    print(f"❌ No camera working at port {i}")

print("\n--- Scan Complete ---")
