import contextlib
from collections import deque
from typing import Self


class TreeNode(object):
    def __init__(self, val: int | None):
        self.val = val
        self.left: Self | None = None
        self.right: Self | None = None

    def __str__(self) -> str:
        return str(self.val)

    def __repr__(self) -> str:
        return f"{self.val}.({self.left} | {self.right})"


def serialize(root: TreeNode | None) -> str:
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str
    """
    serialized = ""
    if not root:
        return serialized

    queue: deque[TreeNode | None] = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            serialized += ","
        else:
            serialized += f"{node.val},"
            queue.append(node.left)
            queue.append(node.right)

    return serialized.rstrip(",")


def deserialize(data: str) -> TreeNode | None:
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """

    if not data:
        return None

    parts = data.split(",")
    root = TreeNode(val=int(parts[0]))

    with contextlib.suppress(IndexError):
        i = 1
        queue = deque([root])
        while queue:
            parent = queue.popleft()
            if parts[i]:
                node = TreeNode(val=int(parts[i]))
                parent.left = node
                queue.append(node)

            i += 1

            if parts[i]:
                node = TreeNode(val=int(parts[i]))
                parent.right = node
                queue.append(node)

            i += 1

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

    return [
        ((parent,), "1,2,3,,,4,5"),
        ((None,), "")
    ]
