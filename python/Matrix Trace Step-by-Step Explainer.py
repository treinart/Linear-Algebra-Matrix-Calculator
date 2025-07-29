# ---/// Matrix Trace Step-by-Step Explainer ///---

from sympy import Matrix, pprint

print("Let's compute the trace of a square matrix!\n")
n = int(input("Enter the matrix size (2-6 for n x n): "))
A = []
for i in range(n):
    row = [float(x) for x in input(f"Row {i+1} (comma-separated): ").split(",")]
    if len(row) != n:
        raise ValueError("Each row must have n entries.")
    A.append(row)
M = Matrix(A)

print("\nStep 1: Your matrix A is:")
pprint(M)

print("\nStep 2: The trace is the sum of diagonal entries.")
trace = sum(M[i, i] for i in range(n))
diag_entries = [M[i, i] for i in range(n)]
print(f"  Diagonal entries: {diag_entries}")
print(f"  Trace = {' + '.join(str(d) for d in diag_entries)} = {trace}")
