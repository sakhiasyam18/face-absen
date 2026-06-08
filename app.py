import cv2

from face_engine.detector import (
    detect_faces
)

from face_engine.face_store import (
    load_embeddings
)

from services.recognition_service import (
    process_recognition
)

load_embeddings()

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        continue

    faces = detect_faces(frame)

    for face in faces:

        box = face.bbox.astype(int)

        x1, y1, x2, y2 = box

        result = process_recognition(
            face.embedding
        )

        status = result.get(
            "status",
            "unknown"
        )

        if status == "attendance_saved":

            label = (
                f"{result['user']['name']} "
                f"[CHECK-IN]"
            )

        elif status == "already_attended":

            label = (
                f"{result['user']['name']} "
                f"[ALREADY]"
            )

        else:

            label = "Unknown"

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            label,
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    cv2.imshow(
        "Attendance System",
        frame
    )

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()