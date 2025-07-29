# ---/// Column Space & Row Space Step-by-Step Explainer ///---

from sympy import Matrix

print("Let's find a basis for the column space and row space of your matrix!\n")
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

print("\nColumn space basis vectors (as columns):")
for idx, v in enumerate(sym_A.columnspace()):
    print(f"  Column {idx+1}: {v}")

print("\nRow space basis vectors (as rows):")
for idx, v in enumerate(sym_A.rowspace()):
    print(f"  Row {idx+1}: {v}")
