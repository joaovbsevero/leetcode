"""
https://leetcode.com/problems/merge-k-sorted-lists/description
"""

import heapq
from typing import Self


class Node:
    def __init__(self, val: int = 0, next: Self | None = None) -> None:
        self.val = val
        self.next = next


def alg(lists: list[Node | None]) -> Node | None:
    out = []
    for node in lists:
        while node:
            heapq.heappush(out, node.val)
            node = node.next

    if not out:
        return None

    head = Node(heapq.heappop(out))
    node = head
    while out:
        node.next = Node(heapq.heappop(out))
        node = node.next
    return head


def run(lists: list[list[int]]) -> list[int]:
    fix_input = []
    for subl in lists:
        node = None
        for val in subl[::-1]:
            current_node = Node(val)
            if node:
                current_node.next = node
            node = current_node
        fix_input.append(node)

    head = alg(fix_input)
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def test_cases():
    return [
        (([[1, 4, 5], [1, 3, 4], [2, 6]],), [1, 1, 2, 3, 4, 4, 5, 6]),
        (([],), []),
        (([[]],), []),
    ]
