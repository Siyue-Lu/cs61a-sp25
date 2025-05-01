def strange_loop():
    """Return a Link s for which s.rest.first.rest is s.

    >>> s = strange_loop()
    >>> s.rest.first.rest is s
    True
    """
    # temp = Link(1, Link(Link(2)))
    # number as first would have a rest, empty doesn't have a rest
    temp = Link(Link.empty, Link(Link(Link.empty)))
    temp.rest.first.rest = temp
    return temp


def sum_rec(s, k):
    """Return the sum of the first k elements in s.

    >>> a = Link(1, Link(6, Link(8)))
    >>> sum_rec(a, 2)
    7
    >>> sum_rec(a, 5)
    15
    >>> sum_rec(Link.empty, 1)
    0
    """
    # Use a recursive call to sum_rec; don't call sum_iter
    if s is Link.empty or k == 0:
        return 0
    return s.first + sum_rec(s.rest, k - 1)

def sum_iter(s, k):
    """Return the sum of the first k elements in s.

    >>> a = Link(1, Link(6, Link(8)))
    >>> sum_iter(a, 2)
    7
    >>> sum_iter(a, 5)
    15
    >>> sum_iter(Link.empty, 1)
    0
    """
    # Don't call sum_rec or sum_iter
    res = 0
    while s is not Link.empty and k > 0:
        res += s.first
        s = s.rest
        k -= 1
    return res


def overlap(s, t):
    """For increasing s and t, count the numbers that appear in both.

    >>> a = Link(3, Link(4, Link(6, Link(7, Link(9, Link(10))))))
    >>> b = Link(1, Link(3, Link(5, Link(7, Link(8)))))
    >>> overlap(a, b)  # 3 and 7
    2
    >>> overlap(a.rest, b)  # just 7
    1
    >>> overlap(Link(0, a), Link(0, b))
    3
    """
    # generator expression, list uses linear search, lookup efficiency O(n)
    # s_list = []
    # t_list = []
    # while s is not Link.empty:
    #     s_list.append(s.first)
    #     s = s.rest
    # while t is not Link.empty:
    #     t_list.append(t.first)
    #     t = t.rest
    # return sum(1 for e in t_list if e in s_list)
    
    # set uses hash table, lookup efficiency O(1)
    # s_set = set()
    # while s is not Link.empty:
    #     s_set.add(s.first)
    #     s = s.rest
    # 
    # cnt = 0
    # while t is not Link.empty:
    #     if t.first in s_set:
    #         cnt += 1
    #     t = t.rest
    # 
    # return cnt
    
    # INCREASING s and t, two pointers, doesn't require extra set or list space
    # cnt = 0
    # while s is not Link.empty and t is not Link.empty:
    #     if s.first < t.first:
    #         s = s.rest
    #     elif s.first > t.first:
    #         t = t.rest
    #     else:
    #         cnt += 1
    #         s = s.rest
    #         t = t.rest
    # return cnt
    
    # recursive two pointers
    if s is Link.empty or t is Link.empty:
        return 0
    elif s.first < t.first:
        return overlap(s.rest, t)
    elif s.first > t.first:
        return overlap(s, t.rest)
    else:
        return 1 + overlap(s.rest, t.rest)


def display(s, k=10):
    """Print the first k digits of infinite linked list s as a decimal.

    >>> s = Link(0, Link(8, Link(3)))
    >>> s.rest.rest.rest = s.rest.rest
    >>> display(s)
    0.8333333333...
    """
    assert s.first == 0, f'{s.first} is not 0'
    digits = f'{s.first}.'
    s = s.rest
    for _ in range(k):
        assert s.first >= 0 and s.first < 10, f'{s.first} is not a digit'
        digits += str(s.first)
        s = s.rest
    print(digits + '...')

def divide(n, d):
    """Return a linked list with a cycle containing the digits of n/d.

    >>> display(divide(5, 6))
    0.8333333333...
    >>> display(divide(2, 7))
    0.2857142857...
    >>> display(divide(1, 2500))
    0.0004000000...
    >>> display(divide(3, 11))
    0.2727272727...
    >>> display(divide(3, 99))
    0.0303030303...
    >>> display(divide(2, 31), 50)
    0.06451612903225806451612903225806451612903225806451...
    """
    assert n > 0 and n < d
    result = Link(0)  # The zero before the decimal point
    cache = {}
    tail = result
    while n not in cache:
        q = n * 10 // d
        r = n * 10 % d
        tail.rest = Link(q)
        tail = tail.rest
        cache[n] = tail
        n = r
    # finds repeated remainder, i.e. start of cycle, point tail to it
    tail.rest = cache[n]
    return result
