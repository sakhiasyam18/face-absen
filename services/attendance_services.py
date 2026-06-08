from database.db import (
    SessionLocal,
    AttendanceLog
)


def save_attendance(
    user_id,
    status="check_in"
):

    session = SessionLocal()

    try:

        attendance = AttendanceLog(
            user_id=user_id,
            status=status
        )

        session.add(attendance)

        session.commit()

        session.refresh(
            attendance
        )

        return attendance

    finally:

        session.close()


def save_checkout(
    user_id
):

    session = SessionLocal()

    try:

        attendance = AttendanceLog(
            user_id=user_id,
            status="check_out"
        )

        session.add(attendance)

        session.commit()

        session.refresh(
            attendance
        )

        return attendance

    finally:

        session.close()