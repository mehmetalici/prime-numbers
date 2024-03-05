from prime_numbers import is_prime, find_primes


def test_is_prime():
    # non-prime number
    val = 10
    assert is_prime(val) == False

    # prime number
    val = 17
    assert is_prime(val) == True

    # corner case
    val = 2
    assert is_prime(val) == True

    # big number
    val = 123123123
    assert is_prime(val) == False

    print("is_prime: All tests passed")


def test_find_primes():
    # normal test 1
    start_after = 5
    count = 3
    primes = find_primes(start_after=start_after, count=count)

    # normal test 2
    start_after = 100
    count = 2
    primes = find_primes(start_after=start_after, count=count)
    assert primes == [101, 103]

    # corner case 1
    start_after = -100
    count = 2
    primes = find_primes(start_after=start_after, count=count)
    assert primes == [2, 3]

    # big number 
    start_after = 12500000
    count = 100
    primes = find_primes(start_after=start_after, count=count)
    print(primes)


    print("find_primes: All tests passed")


if __name__ == "__main__":
    test_is_prime()
    test_find_primes()