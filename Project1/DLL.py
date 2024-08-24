"""
Project 1
CSE 331 S21 (Onsay)
Your Name: Sid Amarnath
DLL.py
"""

from typing import TypeVar, List

# for more information on typehinting, check out https://docs.python.org/3/library/typing.html
T = TypeVar("T")            # represents generic type
Node = TypeVar("Node")      # represents a Node object (forward-declare to use in Node __init__)

# pro tip: PyCharm auto-renders docstrings (the multiline strings under each function definition)
# in its "Documentation" view when written in the format we use here. Open the "Documentation"
# view to quickly see what a function does by placing your cursor on it and using CTRL + Q.
# https://www.jetbrains.com/help/pycharm/documentation-tool-window.html


class Node:
    """
    Implementation of a doubly linked list node.
    Do not modify.
    """
    __slots__ = ["value", "next", "prev"]

    def __init__(self, value: T, next: Node = None, prev: Node = None) -> None:
        """
        Construct a doubly linked list node.

        :param value: value held by the Node.
        :param next: reference to the next Node in the linked list.
        :param prev: reference to the previous Node in the linked list.
        :return: None.
        """
        self.next = next
        self.prev = prev
        self.value = value

    def __repr__(self) -> str:
        """
        Represents the Node as a string.

        :return: string representation of the Node.
        """
        return f"Node({str(self.value)})"

    __str__ = __repr__


class DLL:
    """
    Implementation of a doubly linked list without padding nodes.
    Modify only below indicated line.
    """
    __slots__ = ["head", "tail", "size"]

    def __init__(self) -> None:
        """
        Construct an empty doubly linked list.

        :return: None.
        """
        self.head = self.tail = None
        self.size = 0

    def __repr__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        """
        result = []
        node = self.head
        while node is not None:
            result.append(str(node))
            node = node.next
        return " <-> ".join(result)

    def __str__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        """
        return repr(self)

    # MODIFY BELOW #

    def empty(self) -> bool:
        """
        Return boolean indicating whether DLL is empty.

        Required time & space complexity (respectively): O(1) & O(1).

        :return: True if DLL is empty, else False.
        """
        if self.size == 0:
            return True
        else:
            return False

    def push(self, val: T, back: bool = True) -> None:
        """
        Create Node containing `val` and add to back (or front) of DLL. Increment size by one.

        Required time & space complexity (respectively): O(1) & O(1).

        Note: You might find it easier to implement this as a push_back and
            push_front function first.

        :param val: value to be added to the DLL.
        :param back: if True, add Node containing value to back (tail-end) of DLL;
            if False, add to front (head-end).
        :return: None.
        """
        node_to_push = Node(value=val)
        if self.empty():
            self.head = node_to_push
            self.tail = node_to_push
            node_to_push.prev = None
            node_to_push.next = None
        else:
            if back:
                self.tail.next = node_to_push
                node_to_push.prev = self.tail
                self.tail = node_to_push
                self.tail.next = None   
            else:
                self.head.prev = node_to_push
                node_to_push.next = self.head
                self.head = node_to_push
                self.head.prev = None

        self.size += 1
                
    def pop(self, back: bool = True) -> None:
        """
        Remove Node from back (or front) of DLL. Decrement size by 1. If DLL is empty, do nothing.

        Required time & space complexity (respectively): O(1) & O(1).

        :param back: if True, remove Node from (tail-end) of DLL;
            if False, remove from front (head-end).
        :return: None.
        """
        if self.empty():
            return
        elif self.size == 1:
                node_to_pop = self.head
                self.head = None
                self.tail = None
                self.size -= 1
        else:
            if back:
                node_to_pop = self.tail
                self.tail = node_to_pop.prev
                self.tail.next = None
            else:
                node_to_pop = self.head
                self.head = node_to_pop.next
                self.head.prev = None
                
            self.size -= 1

    def from_list(self, source: List[T]) -> None:
        """
        Construct DLL from a standard Python list.

        Required time & space complexity (respectively): O(n) & O(n).

        :param source: standard Python list from which to construct DLL.
        :return: None.
        """
        for item in source:
            self.push(item)

    def to_list(self) -> List[T]:
        """
        Construct standard Python list from DLL.

        Required time & space complexity (respectively): O(n) & O(n).

        :return: standard Python list containing values stored in DLL.
        """
        dll_list = []
        current_node = self.head
        while current_node:
            dll_list.append(current_node.value)
            current_node = current_node.next
        
        return dll_list

    def find(self, val: T) -> Node:
        """
        Find first instance of `val` in the DLL and return associated Node object.

        Required time & space complexity (respectively): O(n) & O(1).

        :param val: value to be found in DLL.
        :return: first Node object in DLL containing `val`.
            If `val` does not exist in DLL, return None.
        """
        current_node = self.head
        while current_node:
            if current_node.value == val:
                return current_node
            current_node = current_node.next
        
        return None

    def find_all(self, val: T) -> List[Node]:
        """
        Find all instances of `val` in DLL and return Node objects in standard Python list.

        Required time & space complexity (respectively): O(n) & O(n).

        :param val: value to be searched for in DLL.
        :return: Python list of all Node objects in DLL containing `val`.
            If `val` does not exist in DLL, return empty list.
        """
        target_nodes = []
        current_node = self.head
        while current_node:
            if current_node.value == val:
                target_nodes.append(current_node)
            current_node = current_node.next

        return target_nodes

    def _remove_node(self, to_remove: Node) -> None:
        """
        Given a node in the linked list, remove it.
        Should only be called from within the DLL class.

        Required time & space complexity (respectively): O(1) & O(1).

        :param to_remove: node to be removed from the list
        :return: None
        """
        if to_remove == self.head:
            self.pop(back=False)
        elif to_remove == self.tail:
            self.pop(back=True)
        else:
            if to_remove.next is not None:
                to_remove.prev.next = to_remove.next
            if to_remove.prev is not None:
                to_remove.next.prev = to_remove.prev
            self.size -= 1

    def delete(self, val: T) -> bool:
        """
        Delete first instance of `val` in the DLL. Must call _remove_node.

        Required time & space complexity (respectively): O(n) & O(1).

        :param val: value to be deleted from DLL.
        :return: True if Node containing `val` was deleted from DLL; else, False.
        """
        current_node = self.head
        while current_node:
            if current_node.value == val:
                self._remove_node(current_node)
                return True
            current_node = current_node.next
        
        return False

    def delete_all(self, val: T) -> int:
        """
        Delete all instances of `val` in the DLL. Must call _remove_node.

        Required time & space complexity (respectively): O(n) & O(1).

        :param val: value to be deleted from DLL.
        :return: integer indicating the number of Nodes containing `val` deleted from DLL;
                 if no Node containing `val` exists in DLL, return 0.
        """
        deleted_nodes = 0
        current_node = self.head
        while current_node:
            if current_node.value == val:
                self._remove_node(current_node)
                deleted_nodes += 1
            current_node = current_node.next
        
        return deleted_nodes

    def reverse(self) -> None:
        """
        Reverse DLL in-place by modifying all `next` and `prev` references of Nodes in the
        DLL and resetting the `head` and `tail` references.
        Must be implemented in-place for full credit. May not create new Node objects.

        Required time & space complexity (respectively): O(n) & O(1).

        :return: None.
        """
        temp = None
        current_node = self.head
        self.tail = current_node

        while current_node:
            temp = current_node.prev
            current_node.prev = current_node.next
            current_node.next = temp
            current_node = current_node.prev
        
        if temp:
            self.head = temp.prev


def flurricane(dll: DLL, delta: float) -> DLL:
    """
    Applies a moving average filter of width `delta` to the time-series data in `dll`.

    Required time & space complexity (respectively): O(n) & O(N).

    :param dll: A `DLL` where each `Node` holds a `value` of `Tuple(float, float)` representing
                the pair `(t, x)`, where `t` represents the time of some measurement `x`.
    :param delta: A `float` representing the width of the moving average filter to apply.
    :return: A `DLL` holding `Tuple(float, float)` representing `(t, filtered_x)`, where `t` is
             exactly the `t` in the input list, and `filtered_x` is the avg of all measurements
    `x` recorded from `t-delta` to `t` (including endpoints).
    """
    filtered_dll = DLL()

    # base cases
    if dll.empty():
        return filtered_dll
    elif dll.size == 1:
        filtered_dll.push(val=dll.head.value)
    # if delta = 0 -> dll stays same
    elif delta == 0:
        current_node = dll.tail
        while current_node:
            filtered_dll.push(val=current_node.value, back=False)
            current_node = current_node.prev
    else:
        current_node = dll.tail
        while current_node is not None:
            left_node = current_node
            right_node = current_node
            interval = [left_node.value[0] - delta, left_node.value[0]]
            while left_node.prev is not None and left_node.prev.value[0] >= interval[0]:
                left_node = left_node.prev

            total, count = 0, 0
            while right_node != left_node.prev:
                total += right_node.value[1]
                count += 1
                right_node = right_node.prev

            filtered_dll.push(val=(current_node.value[0], total / count), back=False)

            current_node = current_node.prev
            if current_node == dll.head:
                filtered_dll.push(val=current_node.value, back=False)
                current_node = current_node.prev

    return filtered_dll

    
