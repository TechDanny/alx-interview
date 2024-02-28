#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    determines the fewest number of coins needed to meet a given amount
    """
    dp = [total + 1] * (total + 1)
    dp[0] = 0
    if total <= 0:
        return 0

    for x in range(1, total + 1):
        for n in coins:
            if x - n >= 0:
                dp[x] = min(dp[x], 1 + dp[x - n]) if x - n >= 0 else dp[x]
    return dp[total] if dp[total] != total + 1 else -1
