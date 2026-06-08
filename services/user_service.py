from database.db import (
    SessionLocal,
    User,
    AttendanceLog
)

from face_engine.face_store import load_embeddings


def delete_user(user_id):

    session = SessionLocal()

    try:

        user = (
            session.query(User)
            .filter(User.id == user_id)
            .first()
        )

        if not user:
            return False

        session.query(
            AttendanceLog
        ).filter(
            AttendanceLog.user_id == user_id
        ).delete()

        session.delete(user)

        session.commit()
        load_embeddings()

        return True

    finally:
        session.close()