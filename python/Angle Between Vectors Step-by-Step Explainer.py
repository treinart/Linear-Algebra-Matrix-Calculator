# ---/// Angle Between Vectors Step-by-Step Explainer ///---

import math

print("Let's learn how to find the angle between two vectors step by step!\n")
u = [float(x) for x in input("Enter the first vector (comma-separated, e.g. 1,2,3): ").split(",")]
v = [float(x) for x in input("Enter the second vector (same dimension): ").split(",")]

if len(u) != len(v):
    print("Error: Vectors must have same dimension.")
else:
    print("\nStep 1: Compute the dot product u·v:")
    dot = sum(a*b for a, b in zip(u, v))
    for i, (a, b) in enumerate(zip(u, v)):
        print(f"  Entry {i+1}: {a}*{b} = {a*b}")
    print(f"  Sum: {dot}")

    print("\nStep 2: Find the norm (length) of each vector:")
    norm_u = math.sqrt(sum(a**2 for a in u))
    norm_v = math.sqrt(sum(b**2 for b in v))
    print(f"  ||u|| = sqrt(" + " + ".join(f"{a}^2" for a in u) + f") = {norm_u:.5f}")
    print(f"  ||v|| = sqrt(" + " + ".join(f"{b}^2" for b in v) + f") = {norm_v:.5f}")

    if norm_u == 0 or norm_v == 0:
        print("Cannot compute angle with zero vector.")
    else:
        print("\nStep 3: Use the formula: cos(theta) = (u·v) / (||u||*||v||)")
        cos_theta = dot / (norm_u * norm_v)
        print(f"  cos(theta) = {dot:.5f} / ({norm_u:.5f} * {norm_v:.5f}) = {cos_theta:.5f}")
        # Numerical rounding can cause cos_theta to slightly exceed [-1,1]
        cos_theta = min(1.0, max(-1.0, cos_theta))
        theta_rad = math.acos(cos_theta)
        theta_deg = math.degrees(theta_rad)
        print(f"\nStep 4: theta = arccos({cos_theta:.5f}) = {theta_rad:.5f} radians = {theta_deg:.2f} degrees")

        print(f"\nThe angle between your vectors is: {theta_deg:.2f} degrees")
