import argparse
from math import sqrt


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="prime_numbers",
        description="Find 100 prime numbers after a number"
    )
    parser.add_argument("number", help="Number after which to find 100 prime numbers.")
    args = parser.parse_args()
    return args


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
        
    return True


def find_primes(start_after: int, count: int) -> list:
    start = start_after + 1
    primes = []
    
    i = start
    while len(primes) < count:
        if is_prime(i):
            primes.append(i)
        i += 1
    
    return primes


if __name__ == "__main__":
    args = parse_args()
    count = 100
    start_after = int(args.number)
    numbers = find_primes(start_after=start_after, count=count)
    print(numbers)
