"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
You may assume that you have an infinite number of each kind of coin.
The answer is guaranteed to fit into a signed 32-bit integer.

-----------------------------------------

Example 1:

    Input: amount = 5, coins = [1,2,5]
    Output: 4

    Explanation: there are four ways to make up the amount:
        5=5
        5=2+2+1
        5=2+1+1+1
        5=1+1+1+1+1

Example 2:

    Input: amount = 3, coins = [2]
    Output: 0
    Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:

    Input: amount = 10, coins = [10]
    Output: 1

-----------------------------------------

Constraints:

    * 1 <= coins.length <= 300
    * 1 <= coins[i] <= 5000
    * All the values of coins are unique.
    * 0 <= amount <= 5000

-----------------------------------------

Reference: https://leetcode.com/problems/coin-change-ii
"""


def run(coins: list[int], amount: int) -> int:
    # dp[i] represents the number of ways to make amount i
    dp = [0] * (amount + 1)

    # Base case: there is 1 way to make amount 0 (by using no coins)
    dp[0] = 1

    # For each coin, calculate the number of ways to make each amount
    for coin in coins:
        # Update dp array for all amounts that can use this coin
        for i in range(coin, amount + 1):
            # Add the number of ways to make the amount without using the current coin
            dp[i] += dp[i - coin]

    return dp[amount]


def test_cases():
    return [
        (([10], 10), 1),
        (([2], 3), 0),
        (([1, 2, 5], 5), 4),
    ]
