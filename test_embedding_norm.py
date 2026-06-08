from face_engine.face_store import (
    load_embeddings
)

import numpy as np

faces = load_embeddings()

stored_embedding = faces[0]["embedding"]

print(
    "Type:",
    type(stored_embedding)
)

print(
    "Shape:",
    stored_embedding.shape
)

print(
    "Norm:",
    np.linalg.norm(
        stored_embedding
    )
)