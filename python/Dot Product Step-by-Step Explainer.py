# ---/// Dot Product Step-by-Step Explainer ///---

print("Let's learn how to compute the dot product of two vectors step by step!\n")
u = [float(x) for x in input("Enter first vector (e.g. 1,2,3): ").split(",")]
v = [float(x) for x in input("Enter second vector (same dimension): ").split(",")]

if len(u) != len(v):
    print("Error: Vectors must have same dimension.")
else:
    print("\nStep 1: Multiply corresponding entries:")
    terms = []
    for i, (a, b) in enumerate(zip(u, v)):
        prod = a * b
        terms.append(prod)
        print(f"  {u[i]:.2f} * {v[i]:.2f} = {prod:.2f}")
    print("\nStep 2: Add up all products:")
    print("  " + " + ".join(f"{x:.2f}" for x in terms) + f" = {sum(terms):.2f}")
    print(f"\nDot product result: {sum(terms):.2f}")
