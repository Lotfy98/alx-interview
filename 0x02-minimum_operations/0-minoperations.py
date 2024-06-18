#!/usr/bin/python3
'''A module for working with minimum operations.
'''


def minOperations(n):
    if n <= 1:
        return 0
    operations = 0
    for i in range(2, n + 1):
        while n % i == 0:
            operations += i
            n //= i
    return operations
