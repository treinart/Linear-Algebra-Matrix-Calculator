# ---/// Matrix Exponential, Logarithm, Powers Step-by-Step Explainer ///---

from sympy import Matrix, exp, log, pprint

print("Let's compute exp(A), log(A), or A^k for your square matrix!\n")
n = int(input("Enter the matrix size (2-4 for n x n): "))
A = []
for i in range(n):
    row = [float(x) for x in input(f"Row {i+1} (comma-separated): ").split(",")]
    if len(row) != n:
        raise ValueError(f"Each row must have {n} entries.")
    A.append(row)

sym_A = Matrix(A)
print("\nYour matrix A is:")
pprint(sym_A)

choice = input("Choose operation: exp (matrix exponential), log (matrix logarithm), power (A^k): ").lower()

if choice == "exp":
    print("\nStep 1: Compute exp(A) (matrix exponential):")
    pprint(sym_A.exp())
elif choice == "log":
    print("\nStep 1: Compute log(A) (matrix logarithm):")
    pprint(sym_A.log())
elif choice == "power":
    k = int(input("Enter the integer power k: "))
    print(f"\nStep 1: Compute A^{k}:")
    pprint(sym_A**k)
else:
    print("Unknown choice.")
