# ---/// Orthogonal Projection Step-by-Step Explainer (2D, 3D, 4D) ///---

print("Let's project vector u onto vector v step by step.\n")
n = int(input("Enter the dimension (2, 3, or 4): "))

u = [float(x) for x in input("Enter the vector to project (u, comma-separated): ").split(",")]
v = [float(x) for x in input("Enter the vector to project ONTO (v, comma-separated): ").split(",")]

if len(u) != n or len(v) != n:
    raise ValueError(f"Each vector must have {n} entries.")

print("\nStep 1: Compute the dot product u·v and v·v.")
dot_uv = sum(ui*vi for ui,vi in zip(u,v))
dot_vv = sum(vi*vi for vi in v)
print(f"  u·v = " + " + ".join(f"{ui}*{vi}" for ui,vi in zip(u,v)) + f" = {dot_uv}")
print(f"  v·v = " + " + ".join(f"{vi}^2" for vi in v) + f" = {dot_vv}")

if dot_vv == 0:
    print("\nError: The vector v is the zero vector. Cannot project onto the zero vector.")
else:
    coef = dot_uv / dot_vv
    print(f"\nStep 2: Compute the projection coefficient: (u·v)/(v·v) = {dot_uv}/{dot_vv} = {coef}")

    proj = [coef * vi for vi in v]
    print("\nStep 3: Multiply each entry of v by the coefficient to get the projection vector:")
    for i, val in enumerate(proj):
        print(f"  Entry {i+1}: {coef} * {v[i]} = {val}")
    print(f"\nThe orthogonal projection of u onto v is: {proj}")
