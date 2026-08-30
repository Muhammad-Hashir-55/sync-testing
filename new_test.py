"""
Random Number Generator Program
Generates random numbers using Python's built-in `random` module.
"""

import random


def generate_random_number(min_value=1, max_value=100):
    """Generate a single random integer between min_value and max_value (inclusive)."""
    return random.randint(min_value, max_value)


def generate_random_float(min_value=0.0, max_value=1.0):
    """Generate a single random float between min_value and max_value."""
    return random.uniform(min_value, max_value)


def generate_random_list(count=5, min_value=1, max_value=100):
    """Generate a list of `count` random integers between min_value and max_value."""
    return [random.randint(min_value, max_value) for _ in range(count)]


def main():
    print("=== Random Number Generator ===\n")

    # Generate a single random integer between 1 and 100
    single_int = generate_random_number(1, 100)
    print(f"Random integer (1-100): {single_int}")

    # Generate a single random float between 0 and 1
    single_float = generate_random_float(0.0, 1.0)
    print(f"Random float (0.0-1.0): {single_float:.6f}")

    # Generate a list of 5 random integers between 1 and 50
    random_list = generate_random_list(count=5, min_value=1, max_value=50)
    print(f"Random list (5 numbers, 1-50): {random_list}")

    # Pick a random element from a list
    choices = ["apple", "banana", "cherry", "date", "elderberry"]
    picked = random.choice(choices)
    print(f"Random choice from list: {picked}")


if __name__ == "__main__":
    main()