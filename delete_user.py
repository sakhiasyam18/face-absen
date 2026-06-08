from database.db import (
    SessionLocal,
    User,
    AttendanceLog
)

from face_engine.face_store import (
    load_embeddings
)


def delete_all_data():

    session = SessionLocal()

    try:
        session.query(
            AttendanceLog
        ).delete()

        session.query(
            User
        ).delete()

        session.commit()
        load_embeddings()

        print("Data udh di hapus boi")

    except Exception as e:

        session.rollback()

        print(f"Error ngab coba tanya GPT: {e}")

    finally:
        session.close()


if __name__ == "__main__":

    confirm = input(
        "Yakin hapus SEMUA data? (yes/no): "
    )

    if confirm.lower() == "yes":
        delete_all_data()
    else:
        print("Dibatalkan")