import cv2
from ultralytics import YOLO

model = YOLO('C:/Users/ASUS/OneDrive/Desktop/dataset/trash-plastic-bottle-detection-2/runs/detect/train13/weights')

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    confidence_threshold = 0.9

    results = model(frame, conf=confidence_threshold)

    annotated_frame = results[0].plot()

    cv2.imshow('YOLO Detection', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
