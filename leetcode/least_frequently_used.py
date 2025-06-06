"""
Design and implement a data structure for a [Least Frequently Used (LFU)](https://en.wikipedia.org/wiki/Least_frequently_used) cache.

Implement the `LFUCache` class:

  * `LFUCache(int capacity)` Initializes the object with the `capacity` of the data structure.
  * `int get(int key)` Gets the value of the `key` if the key exists in the cache. Otherwise, returns `-1`.
  * `void put(int key, int value)` Update the value of the `key` if present, or inserts the `key` if not already present. When the cache reaches its `capacity`, it should invalidate and remove the **least frequently used** key before inserting a new item. For this problem, when there is a **tie** (i.e., two or more keys with the same frequency), the **least recently used** `key` would be invalidated.

To determine the least frequently used key, a **use counter** is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its **use counter** is set to `1` (due to the `put` operation). The **use counter** for a key in the cache is incremented either a `get` or `put` operation is called on it.

The functions `get` and `put` must each run in `O(1)` average time complexity.

-----------------------------------------

Example 1:

    Input:
      ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
      [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]

    Output: [None, None, None, 1, None, -1, 3, None, -1, 3, 4]

    Explanation:
        // cnt(x) = the use counter for key x
        // cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
        LFUCache lfu = new LFUCache(2);
        lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
        lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
        lfu.get(1);      // return 1
                        // cache=[1,2], cnt(2)=1, cnt(1)=2
        lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                        // cache=[3,1], cnt(3)=1, cnt(1)=2
        lfu.get(2);      // return -1 (not found)
        lfu.get(3);      // return 3
                        // cache=[3,1], cnt(3)=2, cnt(1)=2
        lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                        // cache=[4,3], cnt(4)=1, cnt(3)=2
        lfu.get(1);      // return -1 (not found)
        lfu.get(3);      // return 3
                        // cache=[3,4], cnt(4)=1, cnt(3)=3
        lfu.get(4);      // return 4
                        // cache=[4,3], cnt(4)=2, cnt(3)=3

-----------------------------------------

Constraints:

  * 1 <= capacity <= 104
  * 0 <= key <= 105
  * 0 <= value <= 109
  * At most 2 * 105 calls will be made to get and put.

-----------------------------------------

Reference: https://leetcode.com/problems/lfu-cache
"""

from typing import Generic, Self, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, v: T) -> None:
        self._v = v

        self._next = None
        self._prev = None

    def is_unit(self) -> bool:
        """
        Determine if this node is isolated (i.e., no neighbors).

        Returns:
            bool: True if both prev and next are None (no connections), False otherwise.
        """
        return self._prev is None and self._next is None

    def is_head(self) -> bool:
        """
        Determine if this node is the head (i.e., has no previous node).

        Returns:
            bool: True if this node's prev is None, False otherwise.
        """
        return self._prev is None

    def is_tail(self) -> bool:
        """
        Determine if this node is the tail (i.e., has no next node).

        Returns:
            bool: True if this node's next is None, False otherwise.
        """
        return self._next is None

    def value(self) -> T:
        return self._v

    def set_value(self, v: T) -> None:
        self._v = v

    def next(self) -> Self | None:
        return self._next

    def prev(self) -> Self | None:
        return self._prev

    def set_next(self, next: Self | None) -> None:
        self._next = next

    def set_prev(self, prev: Self | None) -> None:
        self._prev = prev

    def link(self, head: Self) -> None:
        """
        Link this node directly after the given head node in the list.

        This operation will:
            - Set this node's prev to the provided head.
            - If the head already has a next node, rewire that next node's prev to point to this node,
              and set this node's next to that original next node.
            - Finally, set the head's next to this node.

        Args:
            head (Node[T]): The node after which this node should be inserted.
        """

        self._prev = head
        if head_next := head.next():
            # Update myself to point forward to next Node
            self._next = head_next

            # Update next Node to point back to me
            head_next.set_prev(self)

        # Update original Node to point forward to me
        head.set_next(self)

    def unlink(self) -> Self:
        """
        Remove this node from its current position in the list, reconnecting its neighbors.

        This operation will:
            - If there is a previous node, set that node's next to this node's next.
            - If there is a next node, set that node's prev to this node's prev.
            - Set this node's _next and _prev pointers to None.

        Returns:
            Node[T]: The same node instance, now unlinked from its neighbors.
        """

        if self._prev is not None:
            self._prev.set_next(self._next)

        if self._next is not None:
            self._next.set_prev(self._prev)

        self._next = None
        self._prev = None

        return self


class LinkedList(Generic[T]):
    def __init__(self) -> None:
        self.head: Node[T] | None = None
        self.tail: Node[T] | None = None

    def is_empty(self) -> bool:
        """
        Determine if the linked list is empty.

        Returns:
            bool: True if both _head and _tail are None (no nodes in the list), False otherwise.
        """
        return self.head is None and self.tail is None

    def push_back(self, new: Node[T]) -> None:
        """
        Insert a new node at the end (tail) of the list.

        If the list is empty, the new node becomes both head and tail.
        Otherwise, links the new node after the current tail.

        Args:
            new (Node[N]): The node to append to the list.
        """
        if self.is_empty():
            self.head = self.tail = new
        else:
            # Connect the new node after the current tail
            new.link(self.tail)  # type: ignore -> Safety: Non-empty lists always have head and tail
            self.tail = new

    def push_front(self, new: Node[T]) -> None:
        """
        Insert a new node at the beginning (head) of the list.

        If the list is empty, the new node becomes both head and tail.
        Otherwise, links the new node before the current head.

        Args:
            new (Node[N]): The node to prepend to the list.
        """
        if self.is_empty():
            self.head = self.tail = new
        else:
            # Connect the new node before the current head
            self.head.link(new)  # type: ignore -> Safety: Non-empty lists always have head and tail
            self.head = new

    def pop_back(self) -> Node[T]:
        """
        Remove and return the node at the end (tail) of the list.

        Raises:
            IndexError: If the list is empty.

        Returns:
            T: Former tail inner value.
        """

        if self.is_empty():
            raise IndexError("Empty list")

        # Current tail (non-None because list is not empty)
        tail: Node[T] = self.tail  # type: ignore -> Safety: Non-empty lists always have head and tail

        # Update the list's tail reference to the previous node (or None if this was the only node)
        self.tail = tail.prev()
        if self.tail is None:
            # If there's no previous node, list becomes empty
            self.head = None

        # Unlink the old tail from its neighbors
        unlinked = tail.unlink()
        return unlinked

    def pop_front(self) -> Node[T]:
        """
        Remove and return the node at the beginning (head) of the list.

        Raises:
            IndexError: If the list is empty.

        Returns:
            T: Former head inner value.
        """

        if self.is_empty():
            raise IndexError("Empty list")

        # Current head (non-None because list is not empty)
        head: Node[T] = self.head  # type: ignore -> Safety: Non-empty lists always have head and tail

        # Update the list's head reference to the next node (or None if this was the only node)
        self.head = head.next()
        if self.head is None:
            # If there's no next node, list becomes empty
            self.tail = None

        # Unlink the old head from its neighbors
        unlinked = head.unlink()
        return unlinked


class Value:
    def __init__(self, key: int, count: int, value: int) -> None:
        self.count = count
        self.key = key
        self.value = value


class LFUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity

        self._min_count = 1
        self._key_to_node: dict[int, Node[Value]] = {}
        self._count_to_group: dict[int, LinkedList[Value]] = {}

    def _purge(self):
        minimum_group = self._count_to_group[self._min_count]
        node = minimum_group.pop_front()

        self._key_to_node.pop(node.value().key)

        if minimum_group.is_empty():
            # If minimum group is now empty, we need
            # to remove from our dict and update min_count
            # to a new minimum
            self._count_to_group.pop(self._min_count)
            self._min_count = min(self._count_to_group.keys())

    def upgrade_node(self, node: Node[Value]) -> None:
        # Store current value and corresponding group index
        v = node.value()
        old_count = v.count
        old_group = self._count_to_group[old_count]

        if node.is_head():
            # Update LinkedList head to head->next
            old_group.pop_front()
        elif node.is_tail():
            # Update LinkedList tail to head->prev
            old_group.pop_back()
        else:
            # Disconnect from previous LinkedList
            node.unlink()

        # Update value group
        v.count += 1
        if new_group := self._count_to_group.get(v.count):
            new_group.push_back(node)
        else:
            new_group = LinkedList()
            new_group.push_back(node)
            self._count_to_group[v.count] = new_group

        # If we removed the last item from the group
        if old_group.is_empty():
            # Remove the group from our mapping
            self._count_to_group.pop(old_count)

            # If it was also the minimum count that would be purged
            if old_count == self._min_count:
                # Do a small iteration to get next minimum count
                self._min_count = min(self._count_to_group.keys())

    def get(self, key: int) -> int:
        node = self._key_to_node.get(key)
        if node is None:
            return -1

        self.upgrade_node(node)
        return node.value().value

    def put(self, key: int, value: int) -> None:
        # Update currente node value if it exists
        if v := self._key_to_node.get(key):
            old_v = v.value()
            old_v.value = value
            self.upgrade_node(v)
            return

        # Purge if limit was reached
        if len(self._key_to_node) == self._capacity:
            if self._capacity == 1:
                # Handle special case where capacity is 1
                self._key_to_node.clear()
                self._count_to_group.clear()
            else:
                self._purge()

        # Create new Node
        count = 1
        node = Node(Value(key=key, count=count, value=value))

        # Reset min group count to 1
        self._min_count = count

        # Add node to our structures
        self._key_to_node[key] = node
        if group := self._count_to_group.get(count):
            group.push_back(node)
        else:
            group = LinkedList()
            group.push_back(node)
            self._count_to_group[count] = group


def run(
    actions: list[str],
    inputs: list[tuple[int, int] | tuple[int]],
) -> list[int | None]:
    capacity = inputs[0]
    cache = LFUCache(capacity[0])

    outcomes: list[int | None] = [None]
    for action, data in zip(actions[1:], inputs[1:]):
        outcomes.append(getattr(cache, action)(*data))

    return outcomes


def test_cases():
    return [
        (
            (
                [
                    "LFUCache",
                    "put",
                    "put",
                    "get",
                    "get",
                    "get",
                    "put",
                    "put",
                    "get",
                    "get",
                    "get",
                    "get",
                ],
                [
                    [3],
                    [2, 2],
                    [1, 1],
                    [2],
                    [1],
                    [2],
                    [3, 3],
                    [4, 4],
                    [3],
                    [2],
                    [1],
                    [4],
                ],
            ),
            [None, None, None, 2, 1, 2, None, None, -1, 2, 1, 4],
        )
    ]
