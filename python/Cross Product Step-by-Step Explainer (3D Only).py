# ---/// Cross Product Step-by-Step Explainer (3D Only) ///---

print("Let's learn how to compute the cross product of two 3D vectors!\n")
a = [float(x) for x in input("Enter vector A (3 values, e.g. 1,2,3): ").split(",")]
b = [float(x) for x in input("Enter vector B (3 values): ").split(",")]

if len(a) != 3 or len(b) != 3:
    print("Error: Both vectors must have exactly 3 entries.")
else:
    print("\nFormula: A × B = [a2*b3 - a3*b2, a3*b1 - a1*b3, a1*b2 - a2*b1]")
    c1 = a[1]*b[2] - a[2]*b[1]
    c2 = a[2]*b[0] - a[0]*b[2]
    c3 = a[0]*b[1] - a[1]*b[0]
    print(f"  C[1] = {a[1]:.2f}*{b[2]:.2f} - {a[2]:.2f}*{b[1]:.2f} = {c1:.2f}")
    print(f"  C[2] = {a[2]:.2f}*{b[0]:.2f} - {a[0]:.2f}*{b[2]:.2f} = {c2:.2f}")
    print(f"  C[3] = {a[0]:.2f}*{b[1]:.2f} - {a[1]:.2f}*{b[0]:.2f} = {c3:.2f}")
    print(f"\nCross product result: [{c1:.2f}, {c2:.2f}, {c3:.2f}]")
