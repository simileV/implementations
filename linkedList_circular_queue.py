class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass


class CircularQueue:
    """queue implementation using circular linked list for storage"""

    #---------------------------------------------
    class Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next

    # ---------------------------------------------

    def __init__(self):
        self._tail = None
        self._size = 0

    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next