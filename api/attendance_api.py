from flask import (
    Blueprint,
    jsonify
)

from database.db import (
    SessionLocal,
    AttendanceLog,
    User
)

attendance_api = Blueprint(
    "attendance_api",
    __name__
)


@attendance_api.route(
    "/api/attendance"
)
def attendance():

    session = SessionLocal()

    logs = (
        session.query(
            AttendanceLog,
            User
        )
        .join(
            User,
            AttendanceLog.user_id == User.id
        )
        .all()
    )

    result = []

    for log, user in logs:

        result.append(
            {
                "name": user.name,
                "employee_id": user.employee_id,
                "status": log.status,
                "time": str(
                    log.timestamp
                )
            }
        )

    session.close()

    return jsonify(result)