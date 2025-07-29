# ---/// Solve Ax = b Step-by-Step Explainer ///---

import numpy as np
from fractions import Fraction

def print_fraction(val, max_denominator=100):
    f = Fraction(val).limit_denominator(max_denominator)
    return f"{f.numerator}/{f.denominator}" if f.denominator != 1 else f"{f.numerator}"

print("Let's solve the system Ax = b step by step!\n")
n = int(input("Enter the number of equations/unknowns (2-6): "))
print(f"Enter the coefficients of your {n}x{n} matrix A, row by row (comma-separated):")
A = []
for i in range(n):
    row = input(f"Row {i+1}: ").split(",")
    if len(row) != n:
        raise ValueError(f"Row must have {n} entries.")
    A.append([float(x) for x in row])
A = np.array(A, dtype=float)

print(f"\nEnter the entries of your right-hand side vector b (length {n}, comma-separated):")
b = [float(x) for x in input("b: ").split(",")]
if len(b) != n:
    raise ValueError("Vector b must have the same number of entries as rows in A.")
b = np.array(b, dtype=float)

print("\nStep 1: Your system is:")
for i in range(n):
    equation = " + ".join(f"{A[i,j]}*x{j+1}" for j in range(n))
    print(f"  {equation} = {b[i]}")

print("\nStep 2: Write in matrix form: A * x = b")
print("Matrix A:")
for row in A:
    print("   [", "  ".join(f"{x:6.3f}" for x in row), "]")
print(f"Vector b: {b.tolist()}")

detA = np.linalg.det(A)
print(f"\nStep 3: Compute the determinant of A to check if A is invertible: det(A) = {detA:.6f}")

if abs(detA) < 1e-10:
    print("Since det(A) ≈ 0, A is singular and cannot be inverted directly. You may have infinitely many or no solutions.")
else:
    print("Since det(A) ≠ 0, the system has a unique solution.")
    x = np.linalg.solve(A, b)
    print("\nStep 4: Solve for x using A^(-1) * b, or direct Gaussian elimination (NumPy uses both).")
    for i, val in enumerate(x):
        print(f"  x{i+1} = {val:.6f} (or as a fraction: {print_fraction(val)})")

    print("\nStep 5: Verify your solution by plugging x back into A*x:")
    b_check = A.dot(x)
    print("A*x =", b_check.tolist())
    print("Original b:", b.tolist())
    if np.allclose(b_check, b):
        print("✔ Solution verified!")
    else:
        print("✘ Solution does NOT match b. (Check input for typos.)")
