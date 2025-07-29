# ---/// Hadamard Product (Element-wise Matrix Multiplication) Step-by-Step Explainer ///---

import numpy as np

print("Let's compute the Hadamard product (element-wise multiplication) of two matrices!\n")
m, n = map(int, input("Enter matrix size (rows, columns), e.g. 3,3: ").split(","))
A = []
B = []
print("Enter matrix A:")
for i in range(m):
    row = [float(x) for x in input(f"A, Row {i+1}: ").split(",")]
    if len(row) != n:
        raise ValueError("Each row must have n entries.")
    A.append(row)
print("Enter matrix B:")
for i in range(m):
    row = [float(x) for x in input(f"B, Row {i+1}: ").split(",")]
    if len(row) != n:
        raise ValueError("Each row must have n entries.")
    B.append(row)
A = np.array(A)
B = np.array(B)

print("\nStep 1: Both matrices must be the same size.")
print("A =\n", A)
print("B =\n", B)

print("\nStep 2: Multiply corresponding entries (A_ij * B_ij):")
C = A * B
for i in range(m):
    for j in range(n):
        print(f"  ({A[i, j]}) * ({B[i, j]}) = {C[i, j]}")
print("\nHadamard product result:\n", C)
