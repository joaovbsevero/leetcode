"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

-----------------------------------------

Example 1:

    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]
    Explanation: The linked-lists are:
    [
        1->4->5,
        1->3->4,
        2->6
    ]
    merging them into one sorted list:
    1->1->2->3->4->4->5->6

Example 2:

    Input: lists = []
    Output: []
    Example 3:

    Input: lists = [[]]
    Output: []

-----------------------------------------

Constraints:

    * k == lists.length
    * 0 <= k <= 10^4
    * 0 <= lists[i].length <= 500
    * -10^4 <= lists[i][j] <= 10^4
    * lists[i] is sorted in ascending order.
    * The sum of lists[i].length will not exceed 10^4.

-----------------------------------------

Reference: https://leetcode.com/problems/merge-k-sorted-lists
"""

import heapq
from typing import Self


class Node:
    def __init__(self, val: int = 0, next: Self | None = None) -> None:
        self.val = val
        self.next = next


def run(lists: list[Node | None]) -> list[int]:
    """
    This function uses a heap queue to merge multiple sorted linked lists into one sorted linked list.

    At every push, the element pushed will be inserted in the correct position to maintain the heap property. 
    The heap is then used to efficiently retrieve the smallest element from the lists and build the linked
    list in the correct expected order.
    """

    def alg(lists: list[Node | None]) -> Node | None:
        out = []
        for node in lists:
            # For each head inside our, we will push all its values into our heap queue.
            while node:
                heapq.heappush(out, node.val)
                node = node.next

        if not out:
            return None

        # With the heap queue filled, we will start popping the smallest element and building our linked list.
        head = Node(heapq.heappop(out))
        node = head
        while out:
            node.next = Node(heapq.heappop(out))
            node = node.next
        return head

    head = alg(lists)

    # Convert linked list to list
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def test_cases():
    def convert_lists(lists):
        converted_lists = []
        for subl in lists:
            node = None
            for val in subl[::-1]:
                current_node = Node(val)
                if node:
                    current_node.next = node
                node = current_node
            converted_lists.append(node)

        return converted_lists

    return [
        ((convert_lists([[1, 4, 5], [1, 3, 4], [2, 6]]),), [1, 1, 2, 3, 4, 4, 5, 6]),
        (([],), []),
        (([[]],), []),
    ]
