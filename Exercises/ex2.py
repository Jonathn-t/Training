from typing import List

# The goal of this exercise is to find the prime numbers up to 200

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for k in range(2, int(n**0.5) + 1):
        if n % k == 0:
            return False
    return True

def find_prime_numbers(limit: int) -> List[int]:
    """Find and return a list of prime numbers up to a given limit."""
    prime_numbers = []
    for i in range(2, limit + 1):
        if is_prime(i):
            prime_numbers.append(i)
    return prime_numbers


def main() -> None:
    primes = find_prime_numbers(200)
    print(primes)

if __name__ == "__main__":
    main()
