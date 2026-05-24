import math


def get_factorial(k):
    if k == 0:
        return 1
    result = 1
    for i in range(1, k + 1):
        result *= i
    return result


def main():
    print("--- Taylor Series Expansion for e^x ---")

    try:
        x_val = float(input("Enter the exponent value (x): "))
        n_terms = int(input("Enter the number of terms (n): "))

        if n_terms < 1:
            print("Error: Number of terms must be at least 1.")
            return

        a = 0

        approximation = 0.0
        terms_str = []

        for k in range(n_terms):
            numerator = x_val**k
            denominator = get_factorial(k)
            term = numerator / denominator

            approximation += term

            if k == 0:
                terms_str.append("1")
            elif k == 1:
                terms_str.append("x")
            else:
                terms_str.append(f"(x^{k}/{k}!)")

        print("\nOutput:")
        print(
            f"Taylor series expansion of e^x around x={a} up to {n_terms} terms:"
        )
        print(" + ".join(terms_str))

        print("-" * 40)
        print(
            f"Approximated value of e^{x_val} using Taylor series: {approximation:.4f}"
        )

        actual_val = math.exp(x_val)
        print(f"Actual value of e^{x_val}: {actual_val:.4f}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    main()