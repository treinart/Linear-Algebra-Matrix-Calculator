# ---/// Linear Combination Step-by-Step Explainer ///---

print("Let's learn about linear combinations of vectors!\n")
n = int(input("How many vectors do you want to combine? (e.g. 2 or 3): "))
dim = int(input("What is the dimension of each vector? (e.g. 2 or 3): "))

vectors = []
scalars = []

for i in range(n):
    vec = [float(x) for x in input(f"Enter vector {i+1} (comma-separated): ").split(",")]
    if len(vec) != dim:
        raise ValueError(f"Each vector must have {dim} entries.")
    vectors.append(vec)
    scalar = float(input(f"Enter the scalar coefficient for vector {i+1}: "))
    scalars.append(scalar)

print("\nStep 1: Multiply each vector by its scalar coefficient:")
products = []
for i, (c, v) in enumerate(zip(scalars, vectors)):
    product = [c * x for x in v]
    products.append(product)
    print(f"  {c} * {v} = {product}")

print("\nStep 2: Add the resulting vectors entry-wise:")
result = [sum(prod[i] for prod in products) for i in range(dim)]
for i in range(dim):
    entry_sum = " + ".join(f"{prod[i]}" for prod in products)
    print(f"  Entry {i+1}: {entry_sum} = {result[i]}")
print("\nLinear combination result:", result)
