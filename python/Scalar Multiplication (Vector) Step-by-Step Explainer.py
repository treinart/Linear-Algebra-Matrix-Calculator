# ---/// Scalar Multiplication (Vector) Step-by-Step Explainer ///---

from fractions import Fraction

def print_fraction(val, max_denominator=100):
    f = Fraction(val).limit_denominator(max_denominator)
    return f"{f.numerator}/{f.denominator}" if f.denominator != 1 else f"{f.numerator}"

print("Let's learn how to multiply a vector by a scalar!\n")
vec = [float(x) for x in input("Enter your vector (comma-separated, e.g. 2,5,-1): ").split(",")]
scalar = float(input("Enter the scalar: "))

print("\nStep 1: The formula is (scalar * v)[i] = scalar * v[i]")
print(f"Scalar = {scalar}")

print("\nStep 2: Multiply each entry:")
result = []
for i, val in enumerate(vec):
    res = scalar * val
    print(f"  Entry {i+1}: {scalar}*{val:.2f} = {res:.2f} ({print_fraction(res)})")
    result.append(res)
print("\nResult:", result)
