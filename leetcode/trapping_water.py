"""
https://leetcode.com/problems/trapping-rain-water/description/
"""


def run(heights: list[int]) -> int:
    total = 0
    i = 0
    while i < len(heights) - 1:
        if heights[i] == 0:
            i += 1
            continue

        minimum = 0
        while heights[i] > 0:
            local_total = 0
            trapped = False
            j = i + 1
            while j < len(heights):
                if heights[i] > heights[j]:
                    minimum = max(heights[j], minimum)
                    local_total += heights[i] - heights[j]

                elif heights[i] <= heights[j]:
                    trapped = local_total > 0
                    break

                j += 1

            if trapped:
                total += local_total
                i = j
                break

            if heights[i] == minimum:
                break

            heights[i] = minimum

        i += 0 if trapped else 1

    return total


def test_cases():
    return [
        (([3, 2, 4, 2, 3, 2, 3]), 3),
        (([3, 2, 4, 2, 3, 4, 2, 3], 5)),
        (([3, 2, 4]), 1),
        (([4, 2, 3]), 1),
    ]
