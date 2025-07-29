# ---/// Null Space (Kernel) Step-by-Step Explainer ///---

from sympy import Matrix

print("Let's find a basis for the null space (kernel) of a matrix!\n")
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

nulls = sym_A.nullspace()
if not nulls:
    print("\nThe only solution to Ax=0 is the zero vector (nullspace is trivial).")
else:
    print("\nA basis for the nullspace (kernel) of A is:")
    for idx, v in enumerate(nulls):
        print(f"  Nullspace basis vector {idx+1}: {v}")
