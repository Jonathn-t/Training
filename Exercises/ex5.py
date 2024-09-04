# The goal of this exercise is to show the fibonacci numbers up to N

from typing import List

def fibonacci(N: int) -> List[int]:
    """Generate the first N Fibonacci numbers."""
    if N <= 0:
        raise ValueError("N must be a positive integer.")
    
    fib_sequence = [1, 1]

    while len(fib_sequence) < N:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence[:N]

if __name__ == "__main__":
    print(fibonacci(10))