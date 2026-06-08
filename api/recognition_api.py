import base64
import cv2
import numpy as np

from io import BytesIO
from PIL import Image

from flask import (
    Blueprint,
    request,
    jsonify
)

from face_engine.detector import (
    detect_faces
)

from services.recognition_service import (
    process_recognition
)

recognition_api = Blueprint(
    "recognition_api",
    __name__
)


@recognition_api.route(
    "/api/recognize",
    methods=["POST"]
)
def recognize_face():

    try:

        image_data = (
            request.json["image"]
        )

        image_data = (
            image_data.split(",")[1]
        )

        image_bytes = (
            base64.b64decode(
                image_data
            )
        )

        image = Image.open(
            BytesIO(
                image_bytes
            )
        )

        frame = cv2.cvtColor(
            np.array(image),
            cv2.COLOR_RGB2BGR
        )

        faces = detect_faces(
            frame
        )

        if len(faces) == 0:

            return jsonify(
                {
                    "status":
                    "no_face"
                }
            )

        result = process_recognition(
            faces[0].embedding
        )

        return jsonify(
            result
        )

    except Exception as e:

        return jsonify(
            {
                "status":
                "error",
                "message":
                str(e)
            }
        )