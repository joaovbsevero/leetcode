"""
https://leetcode.com/problems/trapping-rain-water/description/
"""


def run(height: list[int]) -> int:
    left = 0
    right = len(height) - 1

    left_max = height[left]
    right_max = height[right]

    water = 0
    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += right_max - height[right]

    return water


def test_cases():
    return [
        (([3, 2, 1, 0],), 0),
        (([3, 2, 4, 2, 3, 2, 3],), 3),
        (([3, 2, 4, 2, 3, 4, 2, 3],), 5),
        (([3, 2, 4],), 1),
        (([4, 2, 3],), 1),
    ]
