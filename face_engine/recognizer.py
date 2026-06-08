import numpy as np

from sklearn.metrics.pairwise import (
    cosine_similarity
)

from face_engine.face_store import (
    known_faces
)


def recognize(
    embedding,
    threshold=0.20
):

    if len(known_faces) == 0:

        print(
            "No registered faces found"
        )

        return None
    
    embedding = np.array(
        embedding,
        dtype=np.float32
    )

    norm = np.linalg.norm(
        embedding
    )

    if norm == 0:

        return None

    embedding = (
        embedding / norm
    ).reshape(1, -1)

    best_match = None
    best_score = -1

    for face in known_faces:

        stored_embedding = np.array(
            face["embedding"],
            dtype=np.float32
        )

        stored_norm = np.linalg.norm(
            stored_embedding
        )

        if stored_norm == 0:
            continue

        stored_embedding = (
            stored_embedding /
            stored_norm
        ).reshape(1, -1)

        score = cosine_similarity(
            embedding,
            stored_embedding
        )[0][0]

        print(
            f"{face['name']} -> {score:.4f}"
        )

        if score > best_score:

            best_score = score
            best_match = face

    if (
        best_match is not None
        and best_score >= threshold
    ):

        print(
            f"Recognized: "
            f"{best_match['name']} "
            f"({best_score:.4f})"
        )

        return {
            "user": best_match,
            "score": float(best_score)
        }

    print(
        f"No match found "
        f"(best score: {best_score:.4f})"
    )

    return None