# ---/// Rule of Sarrus (3x3 Determinant) Step-by-Step Explainer ///---

print("Let's use the Rule of Sarrus to compute the determinant of a 3x3 matrix!\n")
A = []
for i in range(3):
    row = [float(x) for x in input(f"Row {i+1} (comma-separated): ").split(",")]
    if len(row) != 3:
        raise ValueError("Each row must have 3 entries.")
    A.append(row)

print("\nStep 1: Write out the matrix, and repeat the first two columns to the right:")
for row in A:
    print("   ", row, row[:2])

print("\nStep 2: Add the products of the diagonals going down-right:")
d1 = A[0][0] * A[1][1] * A[2][2]
d2 = A[0][1] * A[1][2] * A[2][0]
d3 = A[0][2] * A[1][0] * A[2][1]
print(f"  {A[0][0]}*{A[1][1]}*{A[2][2]} = {d1}")
print(f"  {A[0][1]}*{A[1][2]}*{A[2][0]} = {d2}")
print(f"  {A[0][2]}*{A[1][0]}*{A[2][1]} = {d3}")
sum_down = d1 + d2 + d3

print("\nStep 3: Subtract the products of the diagonals going up-right:")
u1 = A[0][2] * A[1][1] * A[2][0]
u2 = A[0][0] * A[1][2] * A[2][1]
u3 = A[0][1] * A[1][0] * A[2][2]
print(f"  {A[0][2]}*{A[1][1]}*{A[2][0]} = {u1}")
print(f"  {A[0][0]}*{A[1][2]}*{A[2][1]} = {u2}")
print(f"  {A[0][1]}*{A[1][0]}*{A[2][2]} = {u3}")
sum_up = u1 + u2 + u3

det = sum_down - sum_up
print(f"\nStep 4: Determinant = (sum of down-right diagonals) - (sum of up-right diagonals)")
print(f"  Determinant = ({d1} + {d2} + {d3}) - ({u1} + {u2} + {u3}) = {det}")
