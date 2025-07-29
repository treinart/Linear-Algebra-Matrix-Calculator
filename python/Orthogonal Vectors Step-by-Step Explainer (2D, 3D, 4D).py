# ---/// Orthogonal Vectors Step-by-Step Explainer (2D, 3D, 4D) ///---

print("Let's check if two vectors are orthogonal (perpendicular).\n")
n = int(input("Enter the dimension (2, 3, or 4): "))

u = [float(x) for x in input("Enter the first vector (comma-separated): ").split(",")]
v = [float(x) for x in input("Enter the second vector (comma-separated): ").split(",")]

if len(u) != n or len(v) != n:
    raise ValueError(f"Each vector must have {n} entries.")

print("\nStep 1: Compute the dot product u·v = sum of products of corresponding entries.")
dot = 0
for i in range(n):
    prod = u[i]*v[i]
    dot += prod
    print(f"  Entry {i+1}: {u[i]} * {v[i]} = {prod}")

print(f"\nDot product = {dot}")

if abs(dot) < 1e-8:
    print("Result: The vectors ARE orthogonal (dot product is zero).")
else:
    print("Result: The vectors are NOT orthogonal (dot product is not zero).")
