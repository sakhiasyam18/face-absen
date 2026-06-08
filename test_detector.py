import cv2
from face_engine.detector import detect_faces

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    faces = detect_faces(frame)

    print(len(faces))

    cv2.imshow("Test", frame)

    if cv2.waitKey(1) == 27:
        break