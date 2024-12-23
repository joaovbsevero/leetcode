"""
https://leetcode.com/problems/regular-expression-matching/
"""

from functools import lru_cache


@lru_cache(maxsize=512)
def _is_remaining_optional(p: str, p_index: int) -> bool:
    if p_index == len(p):
        return True

    if p[p_index] == "*":
        p_index += 1

    remaining = len(p[p_index:])
    if remaining == 0 or remaining % 2 != 0:
        return False

    return all(p[p_index + pos + 1] == "*" for pos in range(0, remaining, 2))


@lru_cache(maxsize=512)
def _is_match(s: str, s_index: int, p: str, p_index: int) -> bool:
    if s_index == len(s) and p_index == len(p):
        # Exhausted both strings
        return True

    if s_index == len(s):
        # Reached end of string, return True if the remaining
        # of the pattern can be ignored
        return _is_remaining_optional(p=p, p_index=p_index)

    if p_index == len(p):
        return False

    if p[p_index] == "." or p[p_index] == s[s_index]:
        if p_index + 1 < len(p) and p[p_index + 1] == "*":
            if _is_match(s=s, s_index=s_index + 1, p=p, p_index=p_index):
                # Current pattern matched whole remaining string
                return True

            # Current pattern was optional, jump over without advancing string
            return _is_match(s=s, s_index=s_index, p=p, p_index=p_index + 2)

        # Current literal matched pattern literal
        return _is_match(s=s, s_index=s_index + 1, p=p, p_index=p_index + 1)

    if p_index + 1 < len(p) and p[p_index + 1] == "*":
        # Current pattern was optional, jump over without advancing string
        return _is_match(s=s, s_index=s_index, p=p, p_index=p_index + 2)

    return False


def run(s: str, p: str) -> bool:
    return _is_match(s, 0, p, 0)


def test_cases():
    return [
        (("aa", "a"), False),
        (("aa", "a*"), True),
        (("ab", ".*"), True),
    ]
