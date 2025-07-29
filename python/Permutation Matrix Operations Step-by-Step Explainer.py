# ---/// Permutation Matrix Operations Step-by-Step Explainer ///---

from sympy import Matrix, eye, pprint

print("Let's create and apply a permutation matrix!\n")
n = int(input("Enter the size of the square matrix to permute (2-6): "))

print(f"Enter the permutation as a comma-separated list of indices (0-based, e.g. 1,0,2 for swapping first two rows of a 3x3):")
perm = [int(x) for x in input("Permutation: ").split(",")]
if sorted(perm) != list(range(n)):
    raise ValueError("Permutation must be a rearrangement of 0, 1, ..., n-1.")

P = eye(n).permuteBkwd(perm)
print("\nStep 1: The permutation matrix P is:")
pprint(P)

print("\nStep 2: To permute the rows of a matrix A, multiply P*A.")
print("To permute the columns, multiply A*P.T.")
