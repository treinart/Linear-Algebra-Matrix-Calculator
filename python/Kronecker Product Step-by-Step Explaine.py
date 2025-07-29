# ---/// Kronecker Product Step-by-Step Explainer ///---

import numpy as np

print("Let's compute the Kronecker product of two matrices!\n")
m, n = map(int, input("Enter size of matrix A (rows, columns), e.g. 2,2: ").split(","))
A = []
for i in range(m):
    row = [float(x) for x in input(f"A, Row {i+1}: ").split(",")]
    if len(row) != n:
        raise ValueError("Each row must have n entries.")
    A.append(row)
A = np.array(A)

p, q = map(int, input("Enter size of matrix B (rows, columns), e.g. 2,2: ").split(","))
B = []
for i in range(p):
    row = [float(x) for x in input(f"B, Row {i+1}: ").split(",")]
    if len(row) != q:
        raise ValueError("Each row must have q entries.")
    B.append(row)
B = np.array(B)

print("\nStep 1: Write out matrices A and B.")
print("A =\n", A)
print("B =\n", B)

print("\nStep 2: The Kronecker product, A ⊗ B, is formed by multiplying each entry of A by the whole matrix B.")
K = np.kron(A, B)
print("Kronecker product result:\n", K)
