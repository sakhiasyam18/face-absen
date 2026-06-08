from flask import (
    Blueprint,
    jsonify
)

from services.user_service import (
    delete_user
)

delete_bp = Blueprint(
    "delete_user",
    __name__
)


@delete_bp.route(
    "/delete-user/<int:user_id>",
    methods=["DELETE"]
)
def delete_user_route(user_id):

    success = delete_user(user_id)

    if not success:
        return jsonify({
            "status": "error",
            "message": "User not found"
        }), 404

    return jsonify({
        "status": "success"
    })