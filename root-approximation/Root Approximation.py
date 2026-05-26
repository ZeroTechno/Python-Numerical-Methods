import sympy as sp
import numpy as nu
# -------------------------------------------------------
# ROOT APPROXIMATION METHODS
# -------------------------------------------------------

x = sp.Symbol('x')

# Get the function from the user
print("================================")
print("   ROOT APPROXIMATION METHODS   ")
print("================================")
print()
print("Type your function using 'x' as the variable.")
print("Examples:  x**3 - x - 2   |   x**2 - 4   |   x**2 - x - 6")
print()

user_input = input("Enter f(x) = ")
f_expr  = sp.sympify(user_input)
fp_expr = sp.diff(f_expr, x)
f  = sp.lambdify(x, f_expr,  'math')
fp = sp.lambdify(x, fp_expr, 'math')

print()
print(f"f(x)  = {f_expr}")
print()

# Choose method
print("--------------------------------")
print("Select a Method:")
print("  1. Bisection Method")
print("  2. Newton-Raphson Method")
print("  3. Secant Method")
print("--------------------------------")
choice = input("Enter choice (1/2/3): ")
print()

# -------------------------------------------------------
# BISECTION METHOD
# -------------------------------------------------------
if choice == '1':
    print("=== BISECTION METHOD ===")
    print()
    a = float(input("Enter left  value (a): "))
    b = float(input("Enter right value (b): "))
    print()

    if f(a) * f(b) >= 0:
        print("Error: f(a) and f(b) must have opposite signs.")
    else:
        print(f"{'Step':<6} {'a':<14} {'b':<14} {'Midpoint c':<14} {'f(c)':<14}")
        print("-" * 60)

        tol  = 1e-6
        step = 1
        fa   = f(a)

        while (b - a) / 2 > tol:
            c  = (a + b) / 2
            fc = f(c)
            print(f"{step:<6} {a:<14.6f} {b:<14.6f} {c:<14.6f} {fc:<14.6f}")

            if fc == 0:
                break
            elif fa * fc < 0:
                b = c
            else:
                a  = c
                fa = fc
            step += 1

        root = (a + b) / 2
        print()
        print(f"Approximate Root: x = {root:.6f}")
        print(f"Verification:  f({root:.6f}) = {f(root):.2e}")

# -------------------------------------------------------
# NEWTON-RAPHSON METHOD
# -------------------------------------------------------
elif choice == '2':
    print("=== NEWTON-RAPHSON METHOD ===")
    print()
    x0 = float(input("Enter initial guess (x0): "))
    print()

    print(f"{'Step':<6} {'x':<18} {'f(x)':<18} {'Next x':<18}")
    print("-" * 60)

    tol = 1e-6
    xn  = x0

    for step in range(1, 101):
        fxn  = f(xn)
        fpxn = fp(xn)

        if fpxn == 0:
            print("Error: Derivative is zero. Try a different guess.")
            break

        xn1 = xn - fxn / fpxn
        print(f"{step:<6} {xn:<18.8f} {fxn:<18.8f} {xn1:<18.8f}")

        if abs(fxn) < tol:
            break
        xn = xn1

    print()
    print(f"Approximate Root: x = {xn:.6f}")
    print(f"Verification:  f({xn:.6f}) = {f(xn):.2e}")

# -------------------------------------------------------
# SECANT METHOD
# -------------------------------------------------------
elif choice == '3':
    print("=== SECANT METHOD ===")
    print()
    x0 = float(input("Enter first  guess (x0): "))
    x1 = float(input("Enter second guess (x1): "))
    print()

    print(f"{'Step':<6} {'x0':<18} {'x1':<18} {'Next x':<18}")
    print("-" * 60)

    tol = 1e-6

    for step in range(1, 101):
        fx0 = f(x0)
        fx1 = f(x1)

        if abs(fx1) < tol:
            break

        if fx1 - fx0 == 0:
            print("Error: Division by zero. Try different guesses.")
            break

        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        print(f"{step:<6} {x0:<18.8f} {x1:<18.8f} {x2:<18.8f}")
        x0, x1 = x1, x2

    print()
    print(f"Approximate Root: x = {x1:.6f}")
    print(f"Verification:  f({x1:.6f}) = {f(x1):.2e}")

else:
    print("Invalid choice. Please enter 1, 2, or 3.")