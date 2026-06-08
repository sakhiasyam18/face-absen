import cv2

from face_engine.detector import detect_faces
from face_engine.recognizer import recognize
from face_engine.face_store import load_embeddings
import numpy as np
load_embeddings()

cap = cv2.VideoCapture(
    0,
    cv2.CAP_DSHOW
)

while True:

    ret, frame = cap.read()

    if not ret:
        continue

    faces = detect_faces(frame)

    for face in faces:
        print("Recognition Norm:", np.linalg.norm(face.embedding))

        result = recognize(
            face.embedding
        )

        print(result)

    cv2.imshow(
        "Recognition Test",
        frame
    )

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
