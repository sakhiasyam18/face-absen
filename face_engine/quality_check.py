import cv2


def is_blurry(
    frame,
    threshold=15
):

    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    score = cv2.Laplacian(
        gray,
        cv2.CV_64F
    ).var()

    print(
        f"Sharpness Score: {score}"
    )

    result = score < threshold
    print(f"Blur Result: {result}")

    return result