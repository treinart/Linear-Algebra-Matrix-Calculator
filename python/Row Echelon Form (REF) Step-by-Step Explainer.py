# ---/// Row Echelon Form (REF) Step-by-Step Explainer ///---

import numpy as np

print("Let's reduce a matrix to Row Echelon Form (REF) step by step!\n")
m, n = map(int, input("Enter matrix size (rows, columns), e.g. 3,4: ").split(","))
A = []
for i in range(m):
    row = input(f"Row {i+1} (comma-separated): ").split(",")
    if len(row) != n:
        raise ValueError("Each row must have exactly {} entries.".format(n))
    A.append([float(x) for x in row])
A = np.array(A, dtype=float)

def print_matrix(mat):
    for row in mat:
        print("   [", " ".join(f"{x:7.3f}" for x in row), "]")

print("\nOriginal Matrix:")
print_matrix(A)

print("\nStep 1: Apply Gaussian elimination to get REF.")
mat = A.copy()
lead = 0
rows, cols = mat.shape
for r in range(rows):
    if lead >= cols:
        break
    i = r
    while mat[i, lead] == 0:
        i += 1
        if i == rows:
            i = r
            lead += 1
            if cols == lead:
                break
    mat[[r, i]] = mat[[i, r]]
    lv = mat[r, lead]
    if lv != 0:
        mat[r] = mat[r] / lv
        print(f"\n  Row {r+1} divided by {lv} to get leading 1:")
        print_matrix(mat)
    for i in range(r+1, rows):
        lv = mat[i, lead]
        if lv != 0:
            mat[i] = mat[i] - lv * mat[r]
            print(f"\n  Subtract {lv} times row {r+1} from row {i+1}:")
            print_matrix(mat)
    lead += 1

print("\nRow Echelon Form (REF):")
print_matrix(mat)
