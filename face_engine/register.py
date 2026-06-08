import cv2
import pickle
import numpy as np

from face_engine.face_store import (
    load_embeddings
)

from face_engine.detector import (
    detect_faces
)

from face_engine.recognizer import (
    recognize
)

from face_engine.quality_check import (
    is_blurry
)

from database.db import (
    SessionLocal,
    User
)


def register_face(
    name,
    employee_id
):

    load_embeddings()

    session = SessionLocal()

    cap = cv2.VideoCapture(
        0,
        cv2.CAP_DSHOW
    )

    embeddings = []

    print("Camera started")
    print("Collecting 10 face samples...")

    while True:

        ret, frame = cap.read()

        if not ret:
            continue

        key = cv2.waitKey(1) & 0xFF

        if key == 27:
            break

        if is_blurry(
            frame,
            threshold=15
        ):

            cv2.putText(
                frame,
                "Image Too Blurry",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2
            )

            cv2.imshow(
                "Register Face",
                frame
            )

            continue

        faces = detect_faces(frame)

        if len(faces) != 1:

            cv2.putText(
                frame,
                "Show exactly 1 face",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2
            )

            cv2.imshow(
                "Register Face",
                frame
            )

            continue

        face = faces[0]

        embedding = face.embedding

        embedding = (
            embedding /
            np.linalg.norm(
                embedding
            )
        )

        embeddings.append(
            embedding
        )

        print(
            f"Sample {len(embeddings)}/10"
        )

        cv2.putText(
            frame,
            f"Samples: {len(embeddings)}/10",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.imshow(
            "Register Face",
            frame
        )

        if len(embeddings) >= 10:

            break

    if len(embeddings) < 10:

        print(
            "Registration cancelled"
        )

        cap.release()
        cv2.destroyAllWindows()
        session.close()

        return

    existing_employee = (
        session.query(User)
        .filter(
            User.employee_id == employee_id
        )
        .first()
    )

    if existing_employee:

        print(
            "Employee ID already exists"
        )

        cap.release()
        cv2.destroyAllWindows()
        session.close()

        return

    avg_embedding = np.mean(
        embeddings,
        axis=0
    )

    avg_embedding = (
        avg_embedding /
        np.linalg.norm(
            avg_embedding
        )
    )

    user = User(
        name=name,
        employee_id=employee_id,
        embedding=pickle.dumps(
            avg_embedding
        )
    )

    session.add(user)
    session.commit()

    load_embeddings()

    print(
        f"{name} registered successfully"
    )

    cap.release()
    cv2.destroyAllWindows()
    session.close()