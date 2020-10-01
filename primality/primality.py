import random
from primality import miller


def nthprime(nth: int):
    """Returns the nth prime, starting from n = 0, returning 2.

    Arguments:
        {nth} integer -- The {nth} position of the prime

    Raises:
        TypeError -- Wrong type for {nth} parameter, must be integer.
        ValueError -- Wrong value for {nth} integer, must be positive or zero.

    Returns:
        integer -- The {nth} prime.
    """

    if not isinstance(nth, int):
        raise TypeError("nthprime() takes (1) int type parameter. Given: " 
    + str(type(nth)) + '.')
    if nth < 0:
        raise ValueError("nthprime() int parameter must be positive or zero.")
    if nth == 0 or nth == 1:
        return nth + 2
    prime_count = 1
    number = 5
    while True:
        is_prime = miller.miller(number) 
        if is_prime:
            prime_count += 1
            if prime_count == nth:
                return number
        number += 2


def prange(n: int):
    """Returns a list in the form of [2, 3, ..., nth prime].

    Arguments:
        {n} integer -- The lenght of the list.

    Raises:
        TypeError -- Wrong type for {n} parameter, must be integer.
        ValueError -- Wrong value for {n} integer, must be positive or zero.

    Returns:
        List[integer] -- A list of continuous {n} primes, starting from 2.
    """

    if not isinstance(n, int):
        raise TypeError("prange() takes (1) int type parameter. Given: " 
    + str(type(n)) + '.')
    if n < 0:
        raise ValueError("prange() int parameter must be positive or zero.")
    lists = [[], [2], [2,3]]
    if n in (0, 1, 2):
        return lists[n]
    primelist = [2,3]
    number = 5
    while True:
        is_prime = miller.miller(number)
        if is_prime:
            primelist.append(number)
            if len(primelist) == n: 
                return primelist
        number += 2  


def isprime(p: int):
    """True if p is prime.

    Arguments:
        {p} integer -- Integer number.

    Raises:
        TypeError -- Wrong type for {p} parameter, must be integer.

    Returns:
        True -- If {p} is prime.
        False -- If {p} is not prime.
    """

    if not isinstance(p, int):
        raise TypeError("isprime() takes (1) int type parameter. Given: " 
    + str(type(p)) + '.')
    if p in (2,3):
        return True
    if p < 3:
        return False
    return miller.miller(p)