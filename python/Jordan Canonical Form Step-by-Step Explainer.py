# ---/// Jordan Canonical Form Step-by-Step Explainer ///---

from sympy import Matrix, pprint

print("Let's compute the Jordan Canonical Form of a square matrix!\n")
n = int(input("Enter the matrix size (2-4 for n x n; larger sizes may be slow): "))
A = []
for i in range(n):
    row = [float(x) for x in input(f"Row {i+1} (comma-separated): ").split(",")]
    if len(row) != n:
        raise ValueError(f"Each row must have {n} entries.")
    A.append(row)

sym_A = Matrix(A)
print("\nStep 1: Your matrix A is:")
pprint(sym_A)

print("\nStep 2: Find its Jordan form J and the transformation matrix P such that A = P*J*P⁻¹")
J, P = sym_A.jordan_form(calc_transform=True)
print("\nJordan Canonical Form (J):")
pprint(J)
print("\nTransformation matrix (P):")
pprint(P)
print("\nYou can check: P⁻¹*A*P = J")
