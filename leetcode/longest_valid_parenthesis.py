"""
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses
substring.

-----------------------------------------

Example 1:

    Input: s = "(()"
    Output: 2
    Explanation: The longest valid parentheses substring is "()".

Example 2:

    Input: s = ")()())"
    Output: 4
    Explanation: The longest valid parentheses substring is "()()".

Example 3:

    Input: s = ""
    Output: 0

-----------------------------------------

Constraints:

    * 0 <= s.length <= 3 * 10^4
    * s[i] is '(', or ')'.

-----------------------------------------

Reference: https://leetcode.com/problems/longest-valid-parentheses
"""


def run(s: str) -> int:
    """
    The function uses a list `length` to track the lengths of valid parentheses substrings.

    Every time an open parenthesis is encountered, it is added to the list with a value of 0.
    When a close parenthesis is encountered, we collapse to the previous value of the stack, which
    means that subsequent valid parenthesis will collapse all the way to the first value summing
    all the values in between.

    With this approach we also separate non-valid parenthesis since they will be separated by 0s.

    The maximum value in the list is the length of the longest valid parentheses substring.
    """

    length = [0]
    count = 0
    for char in s:
        if char == "(":
            count += 1
            length.append(0)

        elif char == ")" and count:
            count -= 1
            acc = length.pop() + 1
            length[-1] += acc

        else:
            length.append(0)

    return max(length) * 2


def test_cases():
    return [
        (("",), 0),
        (("(",), 0),
        ((")",), 0),
        (("()",), 2),
        (("(()",), 2),
        ((")()",), 2),
        (("())",), 2),
        (("()(",), 2),
        (("(())",), 4),
        (("()()",), 4),
        ((")()())()()(",), 4),
    ]
