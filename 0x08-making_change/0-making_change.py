#!/usr/bin/python3
"""
Change comes from within
"""


from typing import List


def makeChange(coins: list[int], total: int) -> int:
    """
    determines the fewest number of coins needed to meet a given amount
    """
    dp = [total + 1] * (total + 1)
    dp[0] = 0
    for x in range(1, total + 1):
        for n in coins:
            if x - n >= 0:
                dp[x] = min(dp[x], 1 + dp[x - n])
    return dp[total] if dp[total] != total + 1 else -1
