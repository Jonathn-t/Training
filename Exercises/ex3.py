import numpy as np
import matplotlib.pyplot as plt

# The goal of this exercise is to plot the solution of a dynamic system

def dynamic_system_solution(T: float, x0: float, t: np.ndarray) -> np.ndarray:
    """Calculate the solution of the dynamic system x(t) = e^(at) * x0"""
    a = -1 / T
    return np.exp(a * t) * x0

def plot_solution(T: float, x0: float, t_range: tuple) -> None:
    """Plot the solution of the dynamic system over the given time range"""
    t = np.linspace(t_range[0], t_range[1], 500)
    x_t = dynamic_system_solution(T, x0, t)

    # Plotting
    plt.plot(t, x_t)
    plt.title(f'Solution of x(t) for T={T}, x(0)={x0}')
    plt.xlabel('Time (t)')
    plt.ylabel('x(t)')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    T = 5
    x0 = 1
    t_range = (0, 25)
    
    plot_solution(T, x0, t_range)
