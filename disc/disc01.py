def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    # Handle edge cases
    if n <= 1:
        return False  # 0 and 1 are not prime numbers
    if n <= 3:
        return True  # 2 and 3 are prime numbers

    # Eliminate even numbers and multiples of 3 quickly
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check divisors up to the square root of n
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6  # Skip even numbers and multiples of 3
    return True

def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    arr = [False] * 10
    while n > 0:
        arr[n % 10] = True
        n //= 10
    return sum(arr) # sum coverts bool to int

def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    # return str(n).find(str(k)) != -1
    
    # return str(k) in str(n)
    
    while n > 0:
        if n % 10 == k:
            return True
        n //= 10
    return False