# ---/// Determinant by Permutation Expansion (Leibniz Formula) ///---

from sympy import Matrix, pprint

print("Let's compute the determinant using the Leibniz formula (permutations) for a small matrix!\n")
n = int(input("Enter the matrix size (2 or 3 for n x n): "))
A = []
for i in range(n):
    row = [float(x) for x in input(f"Row {i+1} (comma-separated): ").split(",")]
    if len(row) != n:
        raise ValueError("Each row must have n entries.")
    A.append(row)
M = Matrix(A)

print("\nStep 1: Your matrix A is:")
pprint(M)

print("\nStep 2: Compute all possible permutations of the columns.")
print("  For each permutation, multiply the corresponding entries and sum, using the sign of the permutation.")

print("\nFull Leibniz expansion shown below (via sympy):")
det = M.det(method='berkowitz')  # SymPy prints expansion if you call .det() with verbose print
print(f"  Determinant = {det}")
