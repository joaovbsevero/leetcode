"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

-----------------------------------------

Example 1:

    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.

Example 2:

    Input: l1 = [0], l2 = [0]
    Output: [0]

Example 3:

    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]

-----------------------------------------

Constraints:

    * The number of nodes in each linked list is in the range [1, 100].
    * 0 <= Node.val <= 9
    * It is guaranteed that the list represents a number that does not have leading zeros.

-----------------------------------------

Reference: https://leetcode.com/problems/add-two-numbers
"""


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def _build_linked_list_from_list(values: list[int]) -> Node:
    head = Node(val=values[0])
    current = head
    for value in values[1:-1]:
        new = Node(val=value)
        current.next = new
        current = new

    if len(values) > 1:
        current.next = Node(val=values[-1])

    return head


def _run(l1: Node | None, l2: Node | None) -> Node:
    carry = 0
    head = Node()
    current = head
    while True:
        current.val = carry
        if carry:
            # Reset the carried value
            carry = 0

        if l1 is not None:
            # Sum current value from first
            # list
            current.val += l1.val
            l1 = l1.next

        if l2 is not None:
            # Sum current value from second
            # list
            current.val += l2.val
            l2 = l2.next

        if current.val >= 10:
            # Wrap numbers if they go over 10
            # they will never go over 20 given
            # it's always single digits
            carry = 1
            current.val -= 10

        if l1 is None and l2 is None:
            if carry:
                # If there is still a carry
                # add it to the next node
                current.next = Node(val=carry)
            break
        
        # Prepare a new round of sum
        current.next = Node()
        current = current.next

    return head


def run(raw_l1: list[int], raw_l2: list[int]) -> list[int]:
    l1 = _build_linked_list_from_list(raw_l1)
    l2 = _build_linked_list_from_list(raw_l2)

    out = []
    r = _run(l1, l2)
    while r is not None:
        out.append(r.val)
        r = r.next

    return out


def test_cases():
    return [
        # (([2, 4, 3], [5, 6, 4]), [7, 0, 8]),
        # (([0], [0]), [0]),
        (([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]), [8, 9, 9, 9, 0, 0, 0, 1]),
    ]
