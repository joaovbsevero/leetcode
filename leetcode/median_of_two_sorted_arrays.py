"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

-----------------------------------------

Example 1:

    Input: nums1 = [1,3], nums2 = [2]
    Output: 2.00000
    Explanation: merged array = [1,2,3] and median is 2.

Example 2:

    Input: nums1 = [1,2], nums2 = [3,4]
    Output: 2.50000
    Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

-----------------------------------------

Constraints:

    * nums1.length == m
    * nums2.length == n
    * 0 <= m <= 1000
    * 0 <= n <= 1000
    * 1 <= m + n <= 2000
    * -10^6 <= nums1[i], nums2[i] <= 10^6

-----------------------------------------

Reference: https://leetcode.com/problems/median-of-two-sorted-arrays
"""


def run(a: list[int], b: list[int]) -> float:
    """
    This function first determine if the length of the combined list is even or odd.

    If it is even, it means that we are looking for the two values at the middle of
    the merged array.
    Example:
        a: [1, 2]
        b: [3, 4]
        merged: [1, 2, 3, 4]

    We are looking at the indexes 1 and 2 of the merged array (e.g. values 2 and 3).

    If it is odd, it means we are looking at a single value at the middle of the
    merged array.
    Example:
        a: [1, 2]
        b: [3]
        merged: [1, 2, 3]

    We are looking at the index 1 merged array (e.g. value 2).
    """

    def small_generator(a: list[int], b: list[int]):
        """
        Yields the smallest current value from both lists, incrementing the pointer of the list
        that has the smallest value.

        Given that a and b are sorted, it is guaranteed that the output list of values is sorted.
        """

        a_index = 0
        b_index = 0
        while True:
            current_a = None
            if a_index < len(a):
                current_a = a[a_index]

            current_b = None
            if b_index < len(b):
                current_b = b[b_index]

            if current_a and current_b:
                # If both lists still have values, return the smalles between them
                if current_a <= current_b:
                    a_index += 1
                    yield current_a
                else:
                    b_index += 1
                    yield current_b
            elif current_a:
                # If a is longer than b, return the next value from a
                a_index += 1
                yield current_a
            elif current_b:
                # If b is longer than a, return the next value from b
                b_index += 1
                yield current_b
            else:
                # If both lists are exhausted, stop the generator
                # This will never happen since we are stopping at the
                # median, but is checked for completeness
                break

    generator = small_generator(a, b)

    total_length = len(a) + len(b)
    if total_length % 2 == 0:
        median = total_length // 2
        for idx, value in enumerate(generator):
            if idx == median - 1:
                first_value = float(value)
                break
        return (first_value + next(generator)) / 2.0
    else:
        median = int(total_length / 2)
        for idx, value in enumerate(generator):
            if idx == median:
                return float(value)
            
        
    # This will never happen since we are stopping at the
    # median, but to satisfy the linter, we are returning 0.0 here
    return 0.0


def test_cases():
    return [
        (([1, 3], [2]), 2),
        (([1, 2], [3, 4]), 2.5),
    ]
