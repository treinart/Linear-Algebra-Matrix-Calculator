# ---/// Gram-Schmidt Process Step-by-Step Explainer (2D, 3D, 4D) ///---

import numpy as np

print("Let's use the Gram-Schmidt process to orthogonalize a set of vectors step by step!\n")
n = int(input("Enter the dimension of your vectors (2, 3, or 4): "))
k = int(input(f"How many vectors? (up to {n}): "))

vectors = []
for i in range(k):
    vec = [float(x) for x in input(f"Enter vector {i+1} (comma-separated): ").split(",")]
    if len(vec) != n:
        raise ValueError(f"Each vector must have {n} entries.")
    vectors.append(np.array(vec, dtype=float))

print("\nStep 1: List your vectors:")
for i, v in enumerate(vectors):
    print(f"  v{i+1} = {v.tolist()}")

print("\nStep 2: Start the Gram-Schmidt process.")
orthogonal = []
for i, v in enumerate(vectors):
    w = v.copy()
    print(f"\nVector {i+1}: Starting with v{i+1} = {v}")
    for j, u in enumerate(orthogonal):
        proj = np.dot(w, u) / np.dot(u, u) * u
        print(f"  Subtracting projection onto u{j+1}: proj = ({w}·{u})/({u}·{u}) * {u} = {proj}")
        w = w - proj
    orthogonal.append(w)
    print(f"  Resulting orthogonal vector u{i+1} = {w}")

print("\nStep 3: Normalize to get orthonormal vectors (unit vectors):")
orthonormal = []
for i, u in enumerate(orthogonal):
    norm = np.linalg.norm(u)
    if norm != 0:
        e = u / norm
        print(f"  e{i+1} = u{i+1}/||u{i+1}|| = {u}/{norm} = {e}")
        orthonormal.append(e)
    else:
        print(f"  u{i+1} is the zero vector (cannot normalize).")

print("\nYour set of orthogonal (and orthonormal) vectors:")
for i, v in enumerate(orthogonal):
    print(f"  Orthogonal vector u{i+1}: {v}")
for i, v in enumerate(orthonormal):
    print(f"  Orthonormal vector e{i+1}: {v}")
