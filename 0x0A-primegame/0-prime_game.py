#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    if not nums or x <= 0:
        return None

    # Sieve of Eratosthenes to find all primes up to n
    def sieve_of_eratosthenes(n):
        prime = [True] * (n + 1)
        prime[0], prime[1] = False, False  # 0 and 1 are not primes
        p = 2
        while (p * p <= n):
            if prime[p]:
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1
        return prime

    # Maximum number in nums
    max_n = max(nums)

    # Find primes up to max_n using Sieve of Eratosthenes
    primes = sieve_of_eratosthenes(max_n)

    # Precompute the number of primes up to each number
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    # Track the number of wins for each player
    maria_wins = 0
    ben_wins = 0

    # Simulate the game for each number in nums
    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
