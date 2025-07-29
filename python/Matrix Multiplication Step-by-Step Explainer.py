# ---/// Matrix Multiplication Step-by-Step Explainer ///---

import numpy as np

def input_matrix(name, rows, cols):
    print(f"\nEnter the entries for matrix {name} ({rows}x{cols}):")
    mat = []
    for i in range(rows):
        row = input(f"Row {i+1}: ").split(",")
        mat.append([float(x) for x in row])
    return np.array(mat)

print("Let's learn how to multiply matrices (A × B) step by step!\n")

rA, cA = map(int, input("Enter the size of matrix A (rows,columns): ").split(","))
rB, cB = map(int, input("Enter the size of matrix B (rows,columns): ").split(","))
if cA != rB:
    print("Matrix multiplication is only possible when the number of columns of A equals the number of rows of B!")
else:
    A = input_matrix("A", rA, cA)
    B = input_matrix("B", rB, cB)

    print("\nMatrix A:")
    for row in A:
        print("   [", "  ".join(f"{x:.2f}" for x in row), "]")
    print("Matrix B:")
    for row in B:
        print("   [", "  ".join(f"{x:.2f}" for x in row), "]")
    print(f"\nResulting matrix C will be size {rA}x{cB}.\n")

    print("Step 1: For each entry C[i][j], compute the sum of products from the ith row of A and the jth column of B.")
    C = np.zeros((rA, cB))
    for i in range(rA):
        for j in range(cB):
            terms = [f"{A[i,k]:.2f}*{B[k,j]:.2f}" for k in range(cA)]
            products = [A[i,k] * B[k,j] for k in range(cA)]
            print(f"  C[{i+1}][{j+1}] = " + " + ".join(terms) + " = " + " + ".join(f"{x:.2f}" for x in products) + f" = {sum(products):.2f}")
            C[i,j] = sum(products)

    print("\nResult (A × B):")
    for row in C:
        print("   [", "  ".join(f"{x:.2f}" for x in row), "]")
