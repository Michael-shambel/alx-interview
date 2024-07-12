#!/usr/bin/env python3
"""
write a method that calculates the fewest number of operations
 needed to result in exactly nH characters in the file
"""


def minOperations(n):
    if n <= 1:
        return 0

    opration = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            opration += divisor
            n //= divisor
        divisor += 1

    return opration
