from face_engine.recognizer import recognize

from face_engine.attendance_cache import (
    can_attend
)

from services.attendance_services import (
    save_attendance
)


def process_recognition(
    embedding
):

    result = recognize(
        embedding
    )

    if result is None:

        return {
            "status": "unknown"
        }

    user = result["user"]
    user_data = {
        "id": user["id"],
        "name": user["name"],
        "employee_id": user["employee_id"]
    }

    if can_attend(
        user["employee_id"]
    ):

        save_attendance(
            user["id"],
            "check_in"
        )

        return {
            "status":
            "attendance_saved",

            "user":
            user_data,

            "score":
            float(
                result["score"]
            )
        }

    return {
        "status":
        "already_attended",

        "user":
        user_data,

        "score":
        float(
            result["score"]
        )
    }