"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

-----------------------------------------

Example 1:

    Input: coins = [1,2,5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1

Example 2:

    Input: coins = [2], amount = 3
    Output: -1

Example 3:

    Input: coins = [1], amount = 0
    Output: 0

-----------------------------------------

Constraints:

    * 1 <= coins.length <= 12
    * 1 <= coins[i] <= 231 - 1
    * 0 <= amount <= 104

-----------------------------------------

Reference: https://leetcode.com/problems/coin-change
"""

import sys
from functools import cache


def run(coins: list[int], amount: int) -> int:
    """
    Determines the minimum number of coins needed to make up a given amount.

    Args:
        coins (list[int]): A list of integers representing the denominations of the coins.
        amount (int): The total amount of money to make up.

    Returns:
        int: The minimum number of coins needed to make up the given amount. 
             Returns -1 if it is not possible to make up the amount with the given coins.
    """
    @cache
    def recurse(coins: tuple[int], amount: int) -> int:
        if amount < 0 or not coins:
            return -1
        elif amount == 0:
            return 0

        minimum = sys.maxsize
        for coin in coins:
            result = recurse(coins, amount - coin)
            if result != -1 and result < minimum:
                minimum = result + 1

        return minimum if minimum != sys.maxsize else -1

    return recurse(tuple(sorted(coins))[::-1], amount)


def test_cases():
    return [
        (([1, 2, 5], 11), 3),
        (([2], 3), -1),
        (([1], 0), 0),
        (([2, 5, 10, 1], 27), 4),
        (([186, 419, 83, 408], 6249), 20),
    ]
