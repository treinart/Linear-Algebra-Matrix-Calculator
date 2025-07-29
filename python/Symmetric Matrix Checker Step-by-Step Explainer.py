# ---/// Symmetric Matrix Checker Step-by-Step Explainer ///---

import numpy as np

def input_square_matrix():
    n = int(input("Enter the size of your square matrix (e.g. 3 for 3x3): "))
    mat = []
    for i in range(n):
        row = input(f"Row {i+1}: ").split(",")
        mat.append([float(x) for x in row])
    return np.array(mat)

print("Let's learn how to check if a matrix is symmetric!\n")
A = input_square_matrix()

print("\nOriginal Matrix:")
for row in A:
    print("   [", "  ".join(f"{x:.2f}" for x in row), "]")

print("\nStep 1: A matrix is symmetric if A = A^T (equal to its transpose).")
print("Let's compare each off-diagonal entry with its transpose pair.")

n = A.shape[0]
symmetric = True
for i in range(n):
    for j in range(n):
        if A[i, j] != A[j, i]:
            print(f"  Entry ({i+1},{j+1}) = {A[i,j]:.2f} is NOT equal to entry ({j+1},{i+1}) = {A[j,i]:.2f}")
            symmetric = False
        else:
            print(f"  Entry ({i+1},{j+1}) = {A[i,j]:.2f} equals entry ({j+1},{i+1}) = {A[j,i]:.2f}")

if symmetric:
    print("\nResult: The matrix IS symmetric (A = A^T).")
else:
    print("\nResult: The matrix is NOT symmetric.")
