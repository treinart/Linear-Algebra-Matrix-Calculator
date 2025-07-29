# ---/// Block Matrix Operations Step-by-Step Explainer ///---

from sympy import Matrix, BlockMatrix

print("Let's perform block matrix operations!\n")
print("Note: Block matrices are advanced; we'll show how to create and operate on partitioned matrices.")

# Example: 2x2 blocks for a 4x4 matrix
print("For demonstration, enter four 2x2 blocks to form a 4x4 matrix.")

blocks = []
for block_num in range(1, 5):
    block = []
    print(f"Block {block_num} (2x2):")
    for i in range(2):
        row = [float(x) for x in input(f"Row {i+1}: ").split(",")]
        if len(row) != 2:
            raise ValueError("Each row must have 2 entries.")
        block.append(row)
    blocks.append(Matrix(block))

A = BlockMatrix([[blocks[0], blocks[1]], [blocks[2], blocks[3]]])
print("\nYour block matrix A is:")
print(A)

print("\nStep 1: Block matrix multiplication and addition follow matrix algebra rules, but at the block level.")
print("Sympy's BlockMatrix allows you to manipulate the matrix as a block object.")
