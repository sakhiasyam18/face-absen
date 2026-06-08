from flask import (
    Blueprint,
    request,
    jsonify
)

from face_engine.register import (
    register_face
)

register_api = Blueprint(
    "register_api",
    __name__
)


@register_api.route(
    "/api/register",
    methods=["POST"]
)
def register():

    data = request.json

    register_face(
        data["name"],
        data["employee_id"]
    )

    return jsonify(
        {
            "message":
            "success"
        }
    )