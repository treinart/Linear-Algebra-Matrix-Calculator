# ---/// Unit Vector Step-by-Step Explainer ///---

import math
from fractions import Fraction

def print_fraction(val, max_denominator=100):
    f = Fraction(val).limit_denominator(max_denominator)
    return f"{f.numerator}/{f.denominator}" if f.denominator != 1 else f"{f.numerator}"

print("Let's learn how to find the unit vector in the direction of a given vector!\n")
vec = [float(x) for x in input("Enter your vector (comma-separated, e.g. 3,4): ").split(",")]

print("\nStep 1: Find the norm (length) of the vector:")
squares = [x**2 for x in vec]
sum_squares = sum(squares)
length = math.sqrt(sum_squares)
print("    ||v|| = sqrt(" + " + ".join([f"{x:.2f}^2" for x in vec]) + f") = sqrt({sum_squares:.2f}) = {length:.5f}")

if length == 0:
    print("Zero vector has no direction. Cannot compute unit vector.")
else:
    print("\nStep 2: Divide each entry of the vector by its length:")
    unit = [x/length for x in vec]
    for i, (orig, uni) in enumerate(zip(vec, unit)):
        print(f"  Entry {i+1}: {orig:.2f}/{length:.5f} = {uni:.5f} ({print_fraction(uni)})")
    print("\nUnit vector result:", [round(x,5) for x in unit])
