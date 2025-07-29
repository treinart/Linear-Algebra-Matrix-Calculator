# ---/// Cramer's Rule Step-by-Step Explainer ///---

import numpy as np
from fractions import Fraction

def print_fraction(val, max_denominator=100):
    f = Fraction(val).limit_denominator(max_denominator)
    return f"{f.numerator}/{f.denominator}" if f.denominator != 1 else f"{f.numerator}"

print("Let's solve Ax = b using Cramer's Rule, step by step!\n")
n = int(input("Enter the number of equations/unknowns (2-6): "))

print(f"\nEnter the entries for your {n}x{n} matrix A, row by row (comma-separated):")
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

print("\nStep 1: Write the system Ax = b:")
for i in range(n):
    equation = " + ".join(f"{A[i, j]}*x{j+1}" for j in range(n))
    print(f"  {equation} = {b[i]}")

print("\nStep 2: Compute the determinant of A:")
detA = np.linalg.det(A)
print(f"  det(A) = {detA:.6f} (as fraction: {print_fraction(detA)})")

if abs(detA) < 1e-10:
    print("\nSince det(A) ≈ 0, the system has no unique solution. Cramer's Rule does not apply.")
else:
    print("\nStep 3: For each variable, replace the corresponding column of A with b and compute the new determinant.")
    solutions = []
    for k in range(n):
        Ak = np.copy(A)
        Ak[:, k] = b
        detAk = np.linalg.det(Ak)
        print(f"\n  For x{k+1}:")
        print(f"    Replace column {k+1} of A with b:")
        for row in Ak:
            print("     [", "  ".join(f"{x:7.3f}" for x in row), "]")
        print(f"    det(A_{k+1}) = {detAk:.6f} (as fraction: {print_fraction(detAk)})")
        xk = detAk / detA
        print(f"    x{k+1} = det(A_{k+1}) / det(A) = {detAk:.6f} / {detA:.6f} = {xk:.6f} (as fraction: {print_fraction(xk)})")
        solutions.append(xk)
    print("\nStep 4: Solution vector x:")
    for i, val in enumerate(solutions):
        print(f"    x{i+1} = {val:.6f} (as fraction: {print_fraction(val)})")

    print("\nStep 5: Verify your solution by plugging x back into A*x:")
    x_vec = np.array(solutions)
    b_check = A.dot(x_vec)
    print("A*x =", b_check.tolist())
    print("Original b:", b.tolist())
    if np.allclose(b_check, b):
        print("✔ Solution verified!")
    else:
        print("✘ Solution does NOT match b. (Check input for typos.)")

print("\nDone! Now you understand Cramer's Rule for solving systems of equations.")
