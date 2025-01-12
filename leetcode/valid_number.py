"""
Given a string s, return whether s is a valid number.

For example, all the following are valid numbers: "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", while the following are not valid numbers: "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53".

Formally, a valid number is defined using one of the following definitions:

An integer number followed by an optional exponent.
A decimal number followed by an optional exponent.
An integer number is defined with an optional sign '-' or '+' followed by digits.

A decimal number is defined with an optional sign '-' or '+' followed by one of the following definitions:

Digits followed by a dot '.'.
Digits followed by a dot '.' followed by digits.
A dot '.' followed by digits.
An exponent is defined with an exponent notation 'e' or 'E' followed by an integer number.

The digits are defined as one or more digits.

-----------------------------------------

Example 1:

    Input: s = "0"
    Output: true

Example 2:

    Input: s = "e"
    Output: false

Example 3:

    Input: s = "."
    Output: false

-----------------------------------------

Constraints:

    * 1 <= s.length <= 20
    * s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.

-----------------------------------------

Reference: https://leetcode.com/problems/valid-number
"""


def run(s: str) -> bool:
    """
    This functions iterates over the characters of the string s and uses three different
    helper functions to parse the three different "stages" of a number.

    Since number format is sequential, meaning that first we have digits, then we have,
    decimals and finally the exponent, we parse each stage independently one after the other.
    """

    def is_valid_exp(s: str) -> bool:
        """
        Iterate over the characters of s, checking if each character is a digit.
        The function will also check for a valid sign at the beginning of the string.
        """

        if not s:
            return False

        if s[0] in ["-", "+"]:
            s = s[1:]

        if not s:
            return False

        for char in s:
            ascii = ord(char)
            if 47 < ascii < 58:
                continue
            else:
                return False

        return True

    def is_valid_decimal(s: str, has_digit: bool) -> bool:
        """
        Iterate over the characters of s, checking if each character is a digit or a valid decimal point.
        If a decimal point is found, the function will check the remaining characters for validity.
        The function will also check for a valid exponent if an 'e' or 'E' is found.
        The has_digit parameter is used to ensure that at least one digit is present before the decimal point.
        """

        if not s:
            return True

        for idx, char in enumerate(s):
            ascii = ord(char)
            if 47 < ascii < 58:
                has_digit = True
                continue
            elif ascii in [69, 101]:
                return has_digit and is_valid_exp(s[idx + 1 :])
            else:
                return False

        return True

    def is_number(s: str) -> bool:
        """
        Iterate over the characters of s, checking if each character is a digit, decimal point, or exponent.
        The function will also check for a valid sign at the beginning of the string.
        The function will also check for a valid exponent if an 'e' or 'E' is found.
        The has_digit parameter is used to ensure that at least one digit is present before the exponent.
        """

        if not s:
            return False

        if s[0] in ["-", "+"]:
            s = s[1:]

        if not s:
            return False

        has_digit = False
        for idx, char in enumerate(s):
            ascii = ord(char)
            if 47 < ascii < 58:
                has_digit = True
                continue
            elif ascii == 46:
                return len(s) > 1 and is_valid_decimal(s[idx + 1 :], has_digit)
            elif ascii in [69, 101]:
                return has_digit and is_valid_exp(s[idx + 1 :])
            else:
                return False

        return True

    return is_number(s)


def test_cases():
    return [
        (("0",), True),
        ((".",), False),
        ((".1",), True),
        (("e2",), False),
        (("e11",), False),
        ((".e1",), False),
    ]
