# ---/// Matrix/Vector Addition & Subtraction Step-by-Step Explainer ///---

import numpy as np
from fractions import Fraction

def print_fraction(val, max_denominator=100):
    f = Fraction(val).limit_denominator(max_denominator)
    return f"{f.numerator}/{f.denominator}" if f.denominator != 1 else f"{f.numerator}"

def input_matrix(name):
    print(f"\nEnter the size of matrix {name} (rows,columns):")
    m, n = map(int, input("Example: 2,3  means 2 rows, 3 columns: ").split(","))
    print(f"Enter entries for matrix {name}, row by row, separated by commas.")
    mat = []
    for i in range(m):
        row = input(f"Row {i+1}: ").split(",")
        mat.append([float(x) for x in row])
    return np.array(mat)

print("Let's learn how to add and subtract matrices step by step!\n")

# 1. INPUT MATRICES
A = input_matrix("A")
B = input_matrix("B")

if A.shape != B.shape:
    print(f"\nError: Matrices must have the same dimensions to add/subtract.")
    print(f"Matrix A is {A.shape[0]}x{A.shape[1]}, Matrix B is {B.shape[0]}x{B.shape[1]}")
else:
    print("\nOriginal matrices:")
    print("Matrix A:")
    for row in A:
        print("   [", "  ".join(f"{x:.2f}" for x in row), "]")
    print("Matrix B:")
    for row in B:
        print("   [", "  ".join(f"{x:.2f}" for x in row), "]")

    print("\n---\n")
    # 2. EXPLAIN FORMULA
    print("Matrix Addition Formula:")
    print("   (A + B)[i][j] = A[i][j] + B[i][j]")
    print("\nLet's add corresponding entries, step by step:")

    # 3. ADDITION STEP-BY-STEP
    addition = A + B
    for i in range(A.shape[0]):
        row_calc = []
        for j in range(A.shape[1]):
            calc = f"{A[i,j]:.2f} + {B[i,j]:.2f} = {addition[i,j]:.2f}"
            row_calc.append(calc)
        print("   [", " | ".join(row_calc), "]")
    print("\nSum (A + B):")
    for row in addition:
        print("   [", "  ".join(f"{x:.2f}" for x in row), "]")
    print("As fractions:")
    for row in addition:
        print("   [", "  ".join(print_fraction(x) for x in row), "]")

    print("\n---\n")
    print("Matrix Subtraction Formula:")
    print("   (A - B)[i][j] = A[i][j] - B[i][j]")
    print("\nLet's subtract corresponding entries, step by step:")

    # 4. SUBTRACTION STEP-BY-STEP
    subtraction = A - B
    for i in range(A.shape[0]):
        row_calc = []
        for j in range(A.shape[1]):
            calc = f"{A[i,j]:.2f} - {B[i,j]:.2f} = {subtraction[i,j]:.2f}"
            row_calc.append(calc)
        print("   [", " | ".join(row_calc), "]")
    print("\nDifference (A - B):")
    for row in subtraction:
        print("   [", "  ".join(f"{x:.2f}" for x in row), "]")
    print("As fractions:")
    for row in subtraction:
        print("   [", "  ".join(print_fraction(x) for x in row), "]")

# OPTIONAL: Vector Addition/Subtraction
print("\n---")
print("\nNow, let's try **Vector Addition/Subtraction** (2D or 3D vectors):")
print("Enter your vectors as comma-separated values.")
vec1 = [float(x) for x in input("Vector 1 (e.g. 3,4): ").split(",")]
vec2 = [float(x) for x in input("Vector 2 (e.g. 1,2): ").split(",")]

if len(vec1) != len(vec2):
    print("Error: Vectors must have the same dimension.")
else:
    print("\nAddition step-by-step:")
    add = [a + b for a, b in zip(vec1, vec2)]
    print(" + ".join([f"{a}" for a in vec1]) + " + " + " + ".join([f"{b}" for b in vec2]))
    for i in range(len(vec1)):
        print(f"  Entry {i+1}: {vec1[i]:.2f} + {vec2[i]:.2f} = {add[i]:.2f}")
    print("Result:", add)

    print("\nSubtraction step-by-step:")
    sub = [a - b for a, b in zip(vec1, vec2)]
    for i in range(len(vec1)):
        print(f"  Entry {i+1}: {vec1[i]:.2f} - {vec2[i]:.2f} = {sub[i]:.2f}")
    print("Result:", sub)
