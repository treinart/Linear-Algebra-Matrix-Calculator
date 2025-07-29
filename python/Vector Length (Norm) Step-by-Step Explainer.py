# ---/// Vector Length (Norm) Step-by-Step Explainer ///---

import math
from fractions import Fraction

def print_fraction(val, max_denominator=100):
    f = Fraction(val).limit_denominator(max_denominator)
    return f"{f.numerator}/{f.denominator}" if f.denominator != 1 else f"{f.numerator}"

print("Let's learn how to find the length (norm) of a vector step by step!\n")
vec = [float(x) for x in input("Enter your vector (comma-separated, e.g. 3,4): ").split(",")]

print("\nStep 1: Write out the formula for the length of a vector v = [v1, v2, ..., vn]:")
print("    ||v|| = sqrt(v1^2 + v2^2 + ... + vn^2)")

squares = []
for i, val in enumerate(vec):
    sq = val ** 2
    squares.append(sq)
    print(f"  Entry {i+1}: {val}^2 = {sq}")

sum_squares = sum(squares)
print(f"\nStep 2: Sum the squares: { ' + '.join(str(round(x,2)) for x in squares) } = {sum_squares}")

length = math.sqrt(sum_squares)
print(f"\nStep 3: Take the square root: sqrt({sum_squares}) = {length:.5f} ({print_fraction(length)})")

print(f"\nThe norm (length) of your vector is: {length:.5f}")
