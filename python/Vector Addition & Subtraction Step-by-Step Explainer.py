# ---/// Vector Addition & Subtraction Step-by-Step Explainer ///---

from fractions import Fraction

def print_fraction(val, max_denominator=100):
    f = Fraction(val).limit_denominator(max_denominator)
    return f"{f.numerator}/{f.denominator}" if f.denominator != 1 else f"{f.numerator}"

print("Let's learn how to add and subtract vectors step by step!\n")
vec1 = [float(x) for x in input("Enter Vector 1 (comma-separated, e.g. 3,4): ").split(",")]
vec2 = [float(x) for x in input("Enter Vector 2 (same dimension): ").split(",")]

if len(vec1) != len(vec2):
    print("Error: Vectors must have the same dimension.")
else:
    print("\nAddition step-by-step:")
    for i in range(len(vec1)):
        print(f"  Entry {i+1}: {vec1[i]:.2f} + {vec2[i]:.2f} = {vec1[i] + vec2[i]:.2f} ({print_fraction(vec1[i] + vec2[i])})")
    result_add = [a + b for a, b in zip(vec1, vec2)]
    print("Result:", result_add)

    print("\nSubtraction step-by-step:")
    for i in range(len(vec1)):
        print(f"  Entry {i+1}: {vec1[i]:.2f} - {vec2[i]:.2f} = {vec1[i] - vec2[i]:.2f} ({print_fraction(vec1[i] - vec2[i])})")
    result_sub = [a - b for a, b in zip(vec1, vec2)]
    print("Result:", result_sub)
