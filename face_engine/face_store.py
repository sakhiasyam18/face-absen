import pickle

from database.db import (
    SessionLocal,
    User
)

known_faces = []


def load_embeddings():

    global known_faces

    session = SessionLocal()

    try:

        users = session.query(User).all()

        known_faces.clear()

        for user in users:

            known_faces.append({
                "id": user.id,
                "name": user.name,
                "employee_id": user.employee_id,
                "embedding": pickle.loads(
                    user.embedding
                )
            })

        print(
            f"Loaded {len(known_faces)} faces"
        )

        return known_faces

    finally:
        session.close()