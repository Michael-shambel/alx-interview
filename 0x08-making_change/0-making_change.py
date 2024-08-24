#!/usr/bin/python3
"""
pile of coins of different values, determine the fewest number
of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """

    """
    if total <= 0:
        return 0

    dynamicArray = [float('inf')] * (total + 1)
    dynamicArray[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            if dynamicArray[i - 1] != float('inf'):
                dynamicArray[i] = min(
                    dynamicArray[i], dynamicArray[i - coin] + 1)
    if dynamicArray[total] != float('inf'):
        return dynamicArray[total]
    else:
        return -1
