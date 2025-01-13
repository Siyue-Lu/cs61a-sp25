def swipe(n):
    """Print the digits of n, one per line, first backward then forward.

    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    """
    if n < 10:
        print(n)
    else:
        print(n % 10)
        swipe(n // 10)
        print(n % 10)


def skip_factorial(n):
    """Return the product of positive integers n * (n - 2) * (n - 4) * ...

    >>> skip_factorial(5) # 5 * 3 * 1
    15
    >>> skip_factorial(8) # 8 * 6 * 4 * 2
    384
    """
    if n < 3:
        return n
    else:
        return n * skip_factorial(n - 2)


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def helper(divisor):
        # Check divisors up to the square root of n
        if divisor**2 > n:
            return True
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False
        return helper(divisor + 6) # Skip even numbers and multiples of 3

    # Handle edge cases
    if n <= 1:
        return False  # 0 and 1 are not prime numbers
    if n <= 3:
        return True  # 2 and 3 are prime numbers

    # Eliminate even numbers and multiples of 3 quickly
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    return helper(5)


def hailstone(n):
    """Print out the hailstone sequence starting at n,
    and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    print(n)
    if n % 2 == 0:
        return even(n)
    else:
        return odd(n)

def even(n):
    return 1 + hailstone(n // 2)

def odd(n):
    if n == 1:
        return 1
    return 1 + hailstone(n * 3 + 1)


def sevens(n, k):
    """Return the (clockwise) position of who says n among k players.

    >>> sevens(2, 5)
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    >>> sevens(18, 5)
    2
    """
    def f(i, who, direction):
        if i == n:
            return who
        if has_seven(i):
            return f(i + 1, (who - direction) % (k + 1), -direction) # direction as the coefficient of who in next round is the before value, new direction is switched at the end
        else:
            return f(i + 1, (who + direction) % (k + 1), direction)
    return f(1, 1, 1)

def has_seven(n):
    if n == 0:
        return False
    elif n % 10 == 7:
        return True
    else:
        return has_seven(n // 10)

from karel.stanfordkarel import *
def main():
   if front_is_clear():
      move()
      if front_is_clear():
         move()
   # if front_is_clear() is False during previous move(), going into main() would cause skipping moving forwards but one more step moving backwards
   if front_is_clear():
      main()
   if front_is_blocked():
      turn_left()
      turn_left()
   move()