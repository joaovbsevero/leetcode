"""
https://leetcode.com/problems/median-of-two-sorted-arrays/description/
"""

def run(a: list[int], b: list[int]) -> float:
    def find_one(searched_index: int, a: list[int], b: list[int]) -> float:
        a_index = 0
        b_index = 0

        while a_index < len(a) and b_index < len(b):
            if a[a_index] < b[b_index]:
                if a_index + b_index == searched_index:
                    return float(a[a_index])
                a_index += 1
            else:
                if a_index + b_index == searched_index:
                    return float(b[b_index])
                b_index += 1

        if a_index >= len(a):
            while (a_index + b_index) < searched_index:
                b_index += 1
            return float(b[b_index])
        else:
            while (a_index + b_index) < searched_index:
                a_index += 1
            return float(a[a_index])

    def find_two(
        first_index: int, second_index: int, a: list[int], b: list[int]
    ) -> float:
        first_value = find_one(first_index, a, b)
        second_value = find_one(second_index, a, b)
        return (first_value + second_value) / 2.0

    total_length = len(a) + len(b)
    if total_length % 2 == 0:
        median = total_length // 2
        return find_two(median - 1, median, a, b)
    else:
        median = int(total_length / 2)
        return find_one(median, a, b)


def test_cases():
    return [
        (([1, 3], [2]), 2),
        (([1, 2], [3, 4]), 2.5),
    ]
