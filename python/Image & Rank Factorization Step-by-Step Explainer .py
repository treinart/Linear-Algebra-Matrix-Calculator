# ---/// Image & Rank Factorization Step-by-Step Explainer ///---

from sympy import Matrix

print("Let's find the image (column space) and rank factorization of your matrix!\n")
m, n = map(int, input("Enter matrix size (rows, columns), e.g. 3,4: ").split(","))
A = []
for i in range(m):
    row = [float(x) for x in input(f"Row {i+1} (comma-separated): ").split(",")]
    if len(row) != n:
        raise ValueError(f"Each row must have {n} entries.")
    A.append(row)

sym_A = Matrix(A)
print("\nYour matrix A is:")
print(sym_A)

print("\nStep 1: Find a basis for the image (column space).")
col_basis = sym_A.columnspace()
for idx, v in enumerate(col_basis):
    print(f"  Column space basis vector {idx+1}: {v}")

rank = sym_A.rank()
print(f"\nStep 2: The rank of your matrix is: {rank}")

# For factorization: A = C @ R, where C = matrix of basis columns, R = coordinates
print("\nStep 3: Factor A as the product of C (basis) and R (coordinates):")
C = Matrix.hstack(*col_basis)
from sympy import linsolve
R, _ = sym_A.shape
R_mat = sym_A.solve_least_squares(C)
print("C (basis columns):")
print(C)
print("R (coordinates):")
print(R_mat)
print("\nA = C * R (approximately)")
