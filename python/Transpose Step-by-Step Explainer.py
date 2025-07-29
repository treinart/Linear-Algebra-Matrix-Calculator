# ---/// Transpose Step-by-Step Explainer ///---

import numpy as np

def input_matrix():
    print("Enter the matrix size (rows, columns):")
    m, n = map(int, input("Example: 2,3 means 2 rows, 3 columns: ").split(","))
    mat = []
    for i in range(m):
        row = input(f"Row {i+1}: ").split(",")
        mat.append([float(x) for x in row])
    return np.array(mat)

print("Let's learn how to transpose a matrix!\n")
A = input_matrix()

print("\nOriginal Matrix:")
for row in A:
    print("   [", "  ".join(f"{x:.2f}" for x in row), "]")

print("\nStep 1: The transpose of matrix A, written as A^T, is formed by swapping rows and columns.")
print("If A[i][j] is in row i, column j, then in A^T it will be in row j, column i.")

print("\nStep 2: Let's write out each entry's new location:")
m, n = A.shape
AT = A.T
for i in range(m):
    for j in range(n):
        print(f"   A[{i+1}][{j+1}] = {A[i, j]:.2f} moves to A^T[{j+1}][{i+1}]")

print("\nTranspose (A^T):")
for row in AT:
    print("   [", "  ".join(f"{x:.2f}" for x in row), "]")
