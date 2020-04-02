"""O(1) (constant)"""

class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass


class LinkedStack:
    """LIFO stack using a singularly linked list"""

    #---------------------------------------------
    class Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next

    # ---------------------------------------------

    def __init__(self):
        self._head = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        """add elem to top of the stack"""
        self._head = self.Node(e, self._head)
        self._size += 1

    def pop(self):
        """remove and return the elem from the top of the stack, except if empty - LIFO"""
        if self.is_empty():
            raise Empty('stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

    def peek(self):
        """return but do not remove top elem item unless empty"""
        if self.is_empty():
            raise Empty('stack is empty')
        return self._head._element

    def __len__(self):
        return self._size

    # def add_first(self, L, e):
    #     newest = self.Node(e, L.head)
    #     L.head = newest
    #     L.size = L.size + 1
    #
    # def add_last(self, L, e):
    #     newest = self.Node(e, None)
    #     L.tail.next = newest
    #     L.tail = newest
    #     L.size = L.size + 1

    # def remove_first(self, L):
    #     if L.head is None:
    #         raise IndexError('list is empty')
    #     L.head = L.head.next
    #     L.size = L.size - 1