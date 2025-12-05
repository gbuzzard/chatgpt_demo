import math
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    """Function to integrate: f(x) = 1 / (1 + x^2)."""
    return 1.0 / (1.0 + x**2)


def simpsons_rule(f, a, b, n):
    """
    Approximate the integral of f from a to b using Simpson's rule with n subintervals.
    Returns (approx_value, x_nodes, y_nodes).
    """
    if n % 2 == 1:
        raise ValueError("Simpson's rule requires an even number of subintervals (n must be even).")

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)

    # Simpson's rule:
    # integral ≈ (h/3) * [f(x0) + f(xn) + 4 * sum(f(x_odd)) + 2 * sum(f(x_even, internal))]
    S = y[0] + y[-1]
    S += 4.0 * np.sum(y[1:-1:2])  # odd indices
    S += 2.0 * np.sum(y[2:-2:2])  # even indices (internal)

    return (h / 3.0) * S, x, y


def main():
    # Get number of subintervals from user
    n = int(input("Enter the number of subdivisions (n): "))

    # Simpson's rule needs an even number of subintervals
    if n % 2 == 1:
        print("Simpson's rule requires n to be even. Using n + 1 instead.")
        n += 1

    a, b = 0.0, 1.0

    approx, x_nodes, y_nodes = simpsons_rule(f, a, b, n)
    true_value = math.pi / 4.0

    # Create a smooth curve for f(x)
    x_smooth = np.linspace(a, b, 400)
    y_smooth = f(x_smooth)

    fig, ax = plt.subplots(figsize=(8, 5))

    # Plot the true function
    ax.plot(x_smooth, y_smooth, label="f(x) = 1 / (1 + x²)")

    # Plot Simpson's regions as piecewise parabolas
    for i in range(0, n, 2):
        xi = x_nodes[i:i+3]
        yi = y_nodes[i:i+3]

        # Fit a quadratic through (xi, yi)
        coeffs = np.polyfit(xi, yi, 2)
        xp = np.linspace(xi[0], xi[-1], 40)
        yp = np.polyval(coeffs, xp)

        # Fill the region under the quadratic
        ax.fill_between(xp, yp, alpha=0.3)

    # Plot the nodes as points
    ax.plot(x_nodes, y_nodes, 'o', label="Simpson nodes")

    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid(True)

    title = (
        f"Simpson's Rule Approximation (n = {n})\n"
        f"True integral = π/4 ≈ {true_value:.8f}, "
        f"Simpson ≈ {approx:.8f}"
    )
    ax.set_title(title)
    ax.legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()