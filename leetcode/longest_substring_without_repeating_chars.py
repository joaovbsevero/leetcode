"""
Given a string s, find the length of the longest substring without duplicate characters.

-----------------------------------------

Example 1:

    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

Example 2:

    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:

    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3. Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

-----------------------------------------

Constraints:

    * 0 <= s.length <= 5 * 104
    * s consists of English letters, digits, symbols and spaces.

-----------------------------------------

Reference: https://leetcode.com/problems/longest-substring-without-repeating-characters
"""

import contextlib


def run(s: str) -> int:
    biggest = 0
    group = []
    for char in s:
        with contextlib.suppress(ValueError):
            index = group.index(char)
            if len(group) >= biggest:
                biggest = len(group)
            group = group[index + 1 :]

        group.append(char)

    if len(group) >= biggest:
        biggest = len(group)
    return biggest


def test_cases():
    return [
        (("abcabcbb",), 3),
        (("bbbbb",), 1),
        (("pwwkew",), 3),
    ]
