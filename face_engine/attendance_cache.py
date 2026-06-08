from datetime import datetime

attendance_cache = {}


def can_attend(
    employee_id,
    cooldown=60
):

    now = datetime.now()

    if employee_id not in attendance_cache:

        attendance_cache[
            employee_id
        ] = now

        return True

    diff = (
        now -
        attendance_cache[
            employee_id
        ]
    ).total_seconds()

    if diff > cooldown:

        attendance_cache[
            employee_id
        ] = now

        return True

    return False