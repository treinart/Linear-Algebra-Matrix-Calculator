# ---/// Change of Basis Matrix Step-by-Step Explainer ///---

from sympy import Matrix

print("Let's compute the change of basis matrix!\n")
n = int(input("Enter the dimension of the vector space (e.g. 2, 3, or 4): "))

print("\nEnter the OLD basis vectors (as columns), each as comma-separated values:")
old_basis = []
for i in range(n):
    vec = [float(x) for x in input(f"Old basis vector {i+1}: ").split(",")]
    if len(vec) != n:
        raise ValueError("Each basis vector must have n entries.")
    old_basis.append(vec)
P = Matrix(old_basis).T

print("\nEnter the NEW basis vectors (as columns), each as comma-separated values:")
new_basis = []
for i in range(n):
    vec = [float(x) for x in input(f"New basis vector {i+1}: ").split(",")]
    if len(vec) != n:
        raise ValueError("Each basis vector must have n entries.")
    new_basis.append(vec)
Q = Matrix(new_basis).T

print("\nStep 1: Your old basis matrix P is:")
print(P)
print("\nYour new basis matrix Q is:")
print(Q)

print("\nStep 2: The change of basis matrix from old to new basis is:")
change_of_basis = Q.inv() * P
print(change_of_basis)
print("\nTo express a vector in the new basis, multiply the old-basis coordinate vector by this matrix.")
