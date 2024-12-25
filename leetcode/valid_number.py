from functools import lru_cache


class Solution:
    def isValidExp(self, s: str) -> bool:
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

    def isValidDecimal(self, s: str, has_digit: bool) -> bool:
        if not s:
            return True

        for idx, char in enumerate(s):
            ascii = ord(char)
            if 47 < ascii < 58:
                has_digit = True
                continue
            elif ascii in [69, 101]:
                return has_digit and self.isValidExp(s[idx + 1 :])
            else:
                return False

        return True

    def isNumber(self, s: str) -> bool:
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
                return len(s) > 1 and self.isValidDecimal(s[idx + 1 :], has_digit)
            elif ascii in [69, 101]:
                return has_digit and self.isValidExp(s[idx + 1 :])
            else:
                return False

        return True


def run(s: str) -> bool:
    return Solution().isNumber(s)


def test_cases():
    return [
        # (("0",), True),
        # ((".",), False),
        ((".1",), True),
        (("e2",), False),
        (("e11",), False),
        ((".e1",), False),
    ]
