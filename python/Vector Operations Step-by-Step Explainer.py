# ---/// Vector Operations Step-by-Step Explainer ///---

import math
from fractions import Fraction

def print_fraction(val, max_denominator=100):
    f = Fraction(val).limit_denominator(max_denominator)
    return f"{f.numerator}/{f.denominator}" if f.denominator != 1 else f"{f.numerator}"

print("Let's explore common vector operations: add, subtract, scalar multiply, and magnitude.\n")
vec1 = [float(x) for x in input("Enter the first vector (comma-separated): ").split(",")]
vec2 = [float(x) for x in input("Enter the second vector (same size): ").split(",")]

if len(vec1) != len(vec2):
    print("Vectors must have same dimension.")
else:
    print("\nAddition:")
    add = [a + b for a, b in zip(vec1, vec2)]
    for i, (a, b) in enumerate(zip(vec1, vec2)):
        print(f"  Entry {i+1}: {a} + {b} = {a+b}")
    print("  Result:", add)

    print("\nSubtraction:")
    sub = [a - b for a, b in zip(vec1, vec2)]
    for i, (a, b) in enumerate(zip(vec1, vec2)):
        print(f"  Entry {i+1}: {a} - {b} = {a-b}")
    print("  Result:", sub)

    print("\nScalar multiplication (choose a scalar):")
    scalar = float(input("Enter scalar value: "))
    scaled_vec1 = [scalar * x for x in vec1]
    print(f"  {scalar} *", vec1, "=", scaled_vec1)

    print("\nMagnitude (length) of first vector:")
    mag = math.sqrt(sum(x**2 for x in vec1))
    print(f"  sqrt(" + " + ".join(f"{x}^2" for x in vec1) + f") = {mag:.5f} ({print_fraction(mag)})")
