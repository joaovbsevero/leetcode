"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

-----------------------------------------

Example 1:

    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    Explanation: The above elevation map (black section) is represented by array 
    [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

    Input: height = [4,2,0,3,2,5]
    Output: 9
 
-----------------------------------------

Constraints:

    * n == height.length
    * 1 <= n <= 2 * 10^4
    * 0 <= height[i] <= 10^5

-----------------------------------------

Reference: https://leetcode.com/problems/trapping-rain-water
"""


def run(height: list[int]) -> int:
    """
    This function uses two pointers, one at the beginning of the list and one
    at the end of the list. It then calculates the maximum height of the bars
    to the left and right of the current bar. The amount of water that can be
    trapped on top of the current bar is the minimum of the maximum heights
    to the left and right of the current bar minus the height of the current
    bar.

    Intuitively, if the bars result in a triangle shape one can imagine that
    the amount is always cancelling itself because the maximum between the previous
    value and the current will always be the current.

    On another scenario where the bars result in a bowl shape, one can imagine
    that the amount is always summing up, because the maximum between the previous 
    value and the current will always be the previous.
    """

    left_idx = 0
    right_idx = len(height) - 1

    left_max = height[left_idx]
    right_max = height[right_idx]

    water = 0
    while left_idx < right_idx:
        if left_max < right_max:
            left_idx += 1
            left_max = max(left_max, height[left_idx])
            water += left_max - height[left_idx]
        else:
            right_idx -= 1
            right_max = max(right_max, height[right_idx])
            water += right_max - height[right_idx]

    return water


def test_cases():
    return [
        (([3, 2, 1, 0],), 0),
        (([3, 2, 4, 2, 3, 2, 3],), 3),
        (([3, 2, 4, 2, 3, 4, 2, 3],), 5),
        (([3, 2, 4],), 1),
        (([4, 2, 3],), 1),
    ]
