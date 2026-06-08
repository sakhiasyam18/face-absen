from norfair import (
    Detection,
    Tracker
)

tracker = Tracker(
    distance_function="euclidean",
    distance_threshold=30
)


def update_tracker(
    face_boxes
):

    detections = []

    for box in face_boxes:

        x1, y1, x2, y2 = box

        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2

        detections.append(
            Detection(
                points=[
                    [center_x, center_y]
                ]
            )
        )

    return tracker.update(
        detections=detections
    )