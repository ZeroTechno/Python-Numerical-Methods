import math


def main():

    try:
        x = float(input("Enter the point of evaluation (x): "))
        h = float(input("Enter the step size (h): "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    f = lambda val: math.log(val)
    f_prime_exact_val = 1 / x

    forward_diff = (f(x + h) - f(x)) / h

    backward_diff = (f(x) - f(x - h)) / h

    central_diff = (f(x + h) - f(x - h)) / (2 * h)

    err_f = abs(f_prime_exact_val - forward_diff)
    err_b = abs(f_prime_exact_val - backward_diff)
    err_c = abs(f_prime_exact_val - central_diff)

    print("\nExpected Output:\n")
    print(f"Function: f(x) = ln(x)")
    print(f"Point of Evaluation: x = {x}")
    print(f"Step size h = {h}")
    print()

    print(f"Forward Difference: f'({x}) ≈ {forward_diff:.5f}")
    print(f"Backward Difference: f'({x}) ≈ {backward_diff:.5f}")
    print(f"Central Difference: f'({x}) ≈ {central_diff:.5f}")
    print(f"Exact Derivative: f'({x}) = {f_prime_exact_val:.1f}")

    print("\nAbsolute Errors:")
    print(f"Forward: {err_f:.5f}")
    print(f"Backward: {err_b:.5f}")
    print(f"Central: {err_c:.5f}")


if __name__ == "__main__":
    main()