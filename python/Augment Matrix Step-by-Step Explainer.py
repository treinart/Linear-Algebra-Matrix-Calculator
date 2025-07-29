# ---/// Augment Matrix Step-by-Step Explainer ///---

import numpy as np

def input_matrix(name):
    print(f"\nEnter the size of matrix {name} (rows,columns):")
    m, n = map(int, input("Example: 2,3 means 2 rows, 3 columns: ").split(","))
    mat = []
    for i in range(m):
        row = input(f"Row {i+1}: ").split(",")
        mat.append([float(x) for x in row])
    return np.array(mat)

print("Let's learn how to create an augmented matrix!\n")

A = input_matrix("A")
b = []
print("\nNow enter the right-hand side vector/column for augmentation:")
for i in range(A.shape[0]):
    val = float(input(f"b[{i+1}]: "))
    b.append(val)
b = np.array(b).reshape(-1,1)

print("\nStep 1: Write matrices side by side with a divider (|):")
for i in range(A.shape[0]):
    row = "  ".join(f"{A[i,j]:.2f}" for j in range(A.shape[1]))
    print(f"[ {row} | {b[i,0]:.2f} ]")
print("\nAugmented matrix shape:", A.shape[0], "rows x", A.shape[1]+1, "columns")
