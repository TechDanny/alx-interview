#!/usr/bin/python3
"""
Minimum operation
"""


def minOperations(n):
    """
    calculates the fewest number of operations
    """
    if n <= 1:
        return 0
    value = n
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            value = min(value, minOperations(x) + n // x)
    return value
