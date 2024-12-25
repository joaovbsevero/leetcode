from enum import StrEnum, auto
from typing import Self


class TreeNode(object):
    def __init__(self, x: int | None):
        self.val = x
        self.left: Self | None = None
        self.right: Self | None = None

    def __str__(self) -> str:
        return str(self.val)

    def __repr__(self) -> str:
        return f"{self.val}.({self.left} | {self.right})"


class Side(StrEnum):
    LEFT = auto()
    RIGHT = auto()


def serialize(root: TreeNode) -> str:
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str
    """

    current_nodes = [root]
    next_nodes = []

    serialized = f"{root.val},"
    while current_nodes:
        for node in current_nodes:
            if node.left is not None:
                serialized += f"{node.left.val},"
                next_nodes.append(node.left)
            else:
                serialized += "/,"

            if node.right is not None:
                serialized += f"{node.right.val},"
                next_nodes.append(node.right)
            else:
                serialized += "/,"

        current_nodes = next_nodes
        next_nodes = []

    return serialized


def deserialize(data: str) -> TreeNode:
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """

    root = TreeNode(x=None)
    start = 0
    end = 0
    while start < len(data):
        end += 1
        if data[end] == ",":
            break

    data_value = data[start:end]
    if end == start - 1 and data_value[0] == "/":
        current_value = None
    else:
        current_value = int(data[start:end])

    root = TreeNode(current_value)
    if root.val is None:
        return root

    start = end + 1
    side = Side.LEFT
    nodes = [root]
    while start < len(data):
        end += 1
        if data[end] != ",":
            continue

        data_value = data[start:end]
        if start == end - 1 and data_value[0] == "/":
            node = None
        else:
            current_value = int(data[start:end])
            node = TreeNode(current_value)
            nodes.append(node)

        parent = nodes[0]
        if side == Side.LEFT:
            parent.left = node
            side = Side.RIGHT
        else:
            parent.right = node
            side = Side.LEFT
            nodes.pop(0)

        start = end + 1

    return root


def run(root: TreeNode):
    return serialize(deserialize(serialize(root)))


def test_cases():
    left = TreeNode(4)
    right = TreeNode(5)
    parent = TreeNode(3)
    parent.left = left
    parent.right = right
    right = parent
    left = TreeNode(2)
    parent = TreeNode(1)
    parent.left = left
    parent.right = right

    return [((parent,), "1,2,3,/,/,4,5,/,/,/,/,")]
