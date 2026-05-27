import math

def f(x):
    """The function to be integrated: f(x) = 1 / (1 + x^2)"""
    return 1 / (1 + x**2)

def trapezoidal(f, a, b, n):
    """
    Approximates the definite integral using the Trapezoidal Rule.
    """
    h = (b - a) / n
    result = f(a) + f(b)

    for i in range(1, n):
        result += 2 * f(a + i * h)

    return (h / 2) * result

def simpsons_one_third(f, a, b, n):
    """
    Approximates the definite integral using Simpson's 1/3 Rule.
    Note: 'n' must be an even number.
    """
    if n % 2 != 0:
        raise ValueError("Simpson's 1/3 Rule requires an even number of subintervals.")

    h = (b - a) / n
    result = f(a) + f(b)

    for i in range(1, n):
        if i % 2 == 0:
            result += 2 * f(a + i * h)
        else:
            result += 4 * f(a + i * h)

    return (h / 3) * result

def main():
    print("Numerical Integration for f(x) = 1 / (1 + x^2)")


    try:
        a = float(input("Enter the lower limit of integration (Interval) (a): "))
        b = float(input("Enter the upper limit of integration (Interval) (b): "))
        n = int(input("Enter the number of subintervals (n - must be even): "))
    except ValueError:
        print("Invalid input. Please enter numbers for limits and an integer for subintervals.")
        return


    try:
        trap_approx = trapezoidal(f, a, b, n)
        simp_approx = simpsons_one_third(f, a, b, n)
    except ValueError as e:

        print(f"Error: {e}")
        return


    exact_value = math.atan(b) - math.atan(a)


    trap_error = abs(exact_value - trap_approx)
    simp_error = abs(exact_value - simp_approx)


    print("\n--- Results ---")
    print(f"Function: f(x) = 1 / (1 + x^2)")
    print(f"Interval: [{a}, {b}]")
    print(f"Subintervals: {n}")
    print(f"Trapezoidal Rule Approximation: {trap_approx:.5f}")
    print(f"Simpson's 1/3 Rule Approximation: {simp_approx:.5f}")
    print(f"Exact Value: {exact_value:.5f}")
    print(f"Absolute Error (Trapezoidal): {trap_error:.5f}")
    print(f"Absolute Error (Simpson): {simp_error:.5f}")

if __name__ == "__main__":
    main()