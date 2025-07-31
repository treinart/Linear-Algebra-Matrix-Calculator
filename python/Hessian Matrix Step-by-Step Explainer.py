"""
Hessian Matrix Step-by-Step Explainer

This script walks you through calculating the Hessian matrix for a scalar function
of 2 or 3 variables. You'll see all second partial derivatives and explanations.

Author: Travis Reinart
"""

import sympy as sp

def get_variables(n):
    if n == 2:
        return sp.symbols('x y')
    elif n == 3:
        return sp.symbols('x y z')
    else:
        raise ValueError("Only 2 or 3 variables are supported.")

def print_hessian_steps(expr, vars):
    print("\nStep 1: Start with your function f:")
    print(f"    f({', '.join([str(v) for v in vars])}) = {expr}\n")
    
    print("Step 2: Compute all first partial derivatives (the gradient):")
    grad = [sp.diff(expr, v) for v in vars]
    for i, v in enumerate(vars):
        print(f"    ∂f/∂{v} = {grad[i]}")
    print()
    
    print("Step 3: Compute all second partial derivatives:")
    hessian = []
    for i, v1 in enumerate(vars):
        row = []
        for j, v2 in enumerate(vars):
            deriv = sp.diff(grad[i], v2)
            row.append(deriv)
            print(f"    ∂²f/∂{v1}∂{v2} = {deriv}")
        hessian.append(row)
    print()
    
    print("Step 4: Assemble the Hessian matrix:")
    H = sp.Matrix(hessian)
    print(H)
    print()
    print("The Hessian matrix is:")
    sp.pprint(H, use_unicode=True)
    print("\nEach entry [i, j] is the second partial ∂²f/∂xi∂xj.")

def main():
    print("\nHessian Matrix Step-by-Step Explainer")
    print("-" * 40)
    print("Supports functions of 2 or 3 variables (x, y, [z]).\n")
    print("Example input for f(x, y): x**3 + 3*x*y + 2*y**2")
    print("Example input for f(x, y, z): x**2 + y**2 + z**2 + x*y + x*z\n")
    while True:
        n_vars = input("How many variables? Enter 2 or 3: ")
        if n_vars in ['2', '3']:
            n_vars = int(n_vars)
            break
        print("Please enter 2 or 3.")
    vars = get_variables(n_vars)
    expr_str = input(f"Enter your function f({', '.join([str(v) for v in vars])}): ")
    expr = sp.sympify(expr_str)
    print_hessian_steps(expr, vars)
    
    # Optionally evaluate at a point
    eval_choice = input("\nEvaluate the Hessian at a specific point? (y/n): ").strip().lower()
    if eval_choice == 'y':
        subs = {}
        for v in vars:
            val = float(input(f"  Enter value for {v}: "))
            subs[v] = val
        H = sp.hessian(expr, vars)
        evaluated = H.subs(subs)
        print("\nHessian evaluated at your point:")
        sp.pprint(evaluated, use_unicode=True)
    print("\nDone.")

if __name__ == "__main__":
    main()
