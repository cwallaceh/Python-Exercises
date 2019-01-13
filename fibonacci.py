# Python Fibonacci using recursive, dynamic programming and memoization

# fibonacci_recursive function took 556.851 ms
# 832040
# fibonacci_dynamic_programming function took 0.022 ms
# 832040
# fibonacci_memoization function took 0.314 ms
# 832040

from timing import timing


def fibonacci_recursive(n):
    """This function calculates the 'n'th term
    in the fibonacci series recursively
    f(n) = f(n-1) + f(n-2)"""
    # Example:
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

    # Base case
    if n == 0:
        return 0
    elif n < 2:
        return 1
    # Recursion
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_dynamic_programming(n):
    """This function calculates the 'n'th term
    in the fibonacci series using dynamic programming"""

    aux = []

    if n == 0:
        return 0

    for i in range(0, n):
        if i < 2:
            aux.append(1)
        else:
            aux.append(aux[i - 1] + aux[i - 2])
    return aux[i]


def fibonacci_memoization(n, _cache={}):
    """This function calculates the 'n'th term
    in the fibonacci series using memoization"""

    # Base case
    if n == 0:
        return 0
    elif n < 2:
        return 1
    # Recursion
    else:
        if n in _cache:
            return _cache[n]
        else:
            _cache[n] = fibonacci_memoization(n - 1, _cache) + fibonacci_memoization(n - 2, _cache)

    return _cache[n]


n = 30
print(timing(fibonacci_recursive)(n))
print(timing(fibonacci_dynamic_programming)(n))
print(timing(fibonacci_memoization)(n))
