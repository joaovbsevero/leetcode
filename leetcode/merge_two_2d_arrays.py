"""
You are given two 2D integer arrays nums1 and nums2.

    * nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
    * nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.

Each array contains unique ids and is sorted in ascending order by id.

Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:

    * Only ids that appear in at least one of the two arrays should be included in the resulting array.
    * Each id should be included only once and its value should be the sum of the values of this id in the two arrays. If the id does not exist in one of the two arrays, then assume its value in that array to be 0.

Return the resulting array. The returned array must be sorted in ascending order by id.

-----------------------------------------

Example 1:

    Input: nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]
    Output: [[1,6],[2,3],[3,2],[4,6]]
    Explanation: The resulting array contains the following:
    - id = 1, the value of this id is 2 + 4 = 6.
    - id = 2, the value of this id is 3.
    - id = 3, the value of this id is 2.
    - id = 4, the value of this id is 5 + 1 = 6.

Example 2:

    Input: nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]
    Output: [[1,3],[2,4],[3,6],[4,3],[5,5]]
    Explanation: There are no common ids, so we just include each id with its value in the resulting list.

-----------------------------------------

Constraints:

    * 1 <= nums1.length, nums2.length <= 200
    * nums1[i].length == nums2[j].length == 2
    * 1 <= idi, vali <= 1000
    * Both arrays contain unique ids.
    * Both arrays are in strictly ascending order by id.

-----------------------------------------

Reference: https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description
"""

from collections import defaultdict


# Solution without using dictionary, more performant over small sets
def run_small(nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
    if not nums1 and not nums2:
        # Finished consuming both arrays
        return []

    if not nums1:
        # 'nums1' has no more members, use first element from
        # nums2 and continue
        out = [nums2[0]]
        nums2 = nums2[1:]
    elif not nums2:
        # 'nums2' has no more members, use first element from
        # nums1 and continue
        out = [nums1[0]]
        nums1 = nums1[1:]
    else:
        # Both arrays still have values, we will merge the first from both
        # and continue

        id1, val1 = nums1[0]
        id2, val2 = nums2[0]
        if id1 == id2:
            # Both IDs are the same, we will some and advance both
            out = [[id1, val1 + val2]]
            nums1 = nums1[1:]
            nums2 = nums2[1:]
        elif id1 > id2:
            # 'nums1' has a bigger id, we will consume 'nums2' and advance
            out = [[id2, val2]]
            nums2 = nums2[1:]
        else:
            # 'nums2' has a bigger id, we will consume 'nums1' and advance
            out = [[id1, val1]]
            nums1 = nums1[1:]

    if r := run(nums1, nums2):
        out += r

    return out


# Solution using dictionary, more performant over big sets
def run_big(nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
    aux = defaultdict(int)
    for id1, val1 in nums1:
        aux[id1] = val1

    for id2, val2 in nums2:
        aux[id2] += val2

    return [[id, val] for id, val in sorted(aux.items(), key=lambda pair: pair[0])]


def run(nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
    if len(nums1) + len(nums2) > 100:
        return run_big(nums1, nums2)
    else:
        return run_small(nums1, nums2)


def test_cases():
    return [
        (
            ([[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2], [4, 1]]),
            [[1, 6], [2, 3], [3, 2], [4, 6]],
        ),
        (
            ([[2, 4], [3, 6], [5, 5]], [[1, 3], [4, 3]]),
            [[1, 3], [2, 4], [3, 6], [4, 3], [5, 5]],
        ),
    ]
