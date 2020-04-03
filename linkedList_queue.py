"""O(1) (constant)"""


class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass


class LinkedQueue:
    """FIFO queue using linked list for storage"""

    #---------------------------------------------
    class Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next

    # ---------------------------------------------

    def __init__(self):
        """create an empty queue"""
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def dequeue(self):
        """remove the first element of the queue (the one thats been there the longest aka FIFO) unless empty"""

        if self.is_empty():
            raise Empty('queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():  # special case as queue is empty
            self._tail = None  # removed head had also been the tail

    def enqueue(self, e):
        """add elem to back of the queue"""
        newest = self.Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def first(self):
        """return but dont remove the elem at the front of the queue"""
        if self.is_empty():
            raise Empty('queue is empty')
        return self._head._element
