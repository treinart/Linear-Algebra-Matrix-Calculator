# ---/// Minimal Polynomial Step-by-Step Explainer ///---

from sympy import Matrix, symbols

print("Let's find the minimal polynomial of a square matrix!\n")
n = int(input("Enter the matrix size (2-4 for n x n): "))
A = []
for i in range(n):
    row = [float(x) for x in input(f"Row {i+1} (comma-separated): ").split(",")]
    if len(row) != n:
        raise ValueError(f"Each row must have {n} entries.")
    A.append(row)

sym_A = Matrix(A)
print("\nStep 1: Your matrix A is:")
print(sym_A)

print("\nStep 2: The minimal polynomial is the monic polynomial p(x) of least degree such that p(A) = 0.")
min_poly = sym_A.minimal_polynomial()
print("\nMinimal polynomial of A is:")
print(min_poly)
