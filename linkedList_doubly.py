class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass


class LinkedList_doubly:
    """doubly linked list"""

    #---------------------------------------------
    class Node:
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    # ---------------------------------------------

    def __init__(self):
        """create an empty list with 'sentinel' header and trailer"""
        self._header = self.Node(None, None, None)
        self._trailer = self.Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def insert_between(self, e, predecessor, successor):
        """add elem between two nodes and return it"""
        newest = self.Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def delete_node(self, node):
        """delete non-sentinel node and return its elem"""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

    def is_empty(self):
        return self._size == 0