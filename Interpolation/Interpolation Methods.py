import numpy as np
from scipy.interpolate import CubicSpline


def direct_method(x, y, xt):
    coeffs = np.linalg.solve(np.vander(x, increasing=False), y)
    return np.polyval(coeffs, xt)


def divided_difference_table(x, y):
    n = len(x)
    coef = y.copy().astype(float)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x[i] - x[i - j])
    return coef


def newton_divided_difference(x, y, xt):
    coef = divided_difference_table(x, y)
    n = len(x)
    result = coef[-1]
    for i in range(n - 2, -1, -1):
        result = result * (xt - x[i]) + coef[i]
    return result


def lagrange_interpolation(x, y, xt):
    n = len(x)
    result = 0.0
    for i in range(n):
        L_i = 1.0
        for j in range(n):
            if j != i:
                L_i *= (xt - x[j]) / (x[i] - x[j])
        result += y[i] * L_i
    return result


def spline_interpolation(x, y, xt):
    return float(CubicSpline(x, y)(xt))


def main():
    print("=" * 50)
    print("  Polynomial Approximation & Interpolation")
    print("=" * 50)

    n = int(input("\nNumber of data points: ").strip())
    x = np.array(input(f"Enter {n} x values (space-separated): ").split(), dtype=float)
    y = np.array(input(f"Enter {n} y values (space-separated): ").split(), dtype=float)
    xt = float(input("Test value x_t: ").strip())

    results = {
        "Direct Method":               direct_method(x, y, xt),
        "Newton's Divided Difference": newton_divided_difference(x, y, xt),
        "Lagrange Interpolation":      lagrange_interpolation(x, y, xt),
        "Spline Interpolation":        spline_interpolation(x, y, xt),
    }

    print(f"\nInterpolated value at x_t = {xt}:")
    for method, value in results.items():
        print(f"  {method:<30}: {round(value, 2)}")
    print()


if __name__ == "__main__":
    main()