import matplotlib.pyplot as plt
import numpy as np

# The goal of this exercise is to plot the cosine and sine of x

def plot_function(x: np.ndarray, y: np.ndarray, title: str) -> None:
    """Plots a function with the given x and y values and a title."""
    plt.plot(x, y)
    plt.title(title)
    plt.grid()


def main() -> None:
    x = np.arange(0, 2 * np.pi, 0.1)

    plt.subplot(2, 1, 1)
    plot_function(x, np.cos(x), "Cos(x)")

    plt.subplot(2, 1, 2)
    plot_function(x, np.sin(x), "Sin(x)")

    plt.show()

if __name__ == "__main__":
    main()
