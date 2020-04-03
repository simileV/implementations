# can insert a node at either end and can delete a node at the front
# cannot efficiently delete a node from the tail
# cannot delete a node from an interior position of the list if only given ref to that node because you dont store
# the preceding node, only the next one


class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


class Node:
    def __init__(self, element, next):
        self._element = element
        self._next = next

    def add_first(self, L, e):
        newest = Node(e, L.head)
        L.head = newest
        L.size = L.size + 1

    def add_last(self, L, e):
        newest = Node(e, None)
        L.tail.next = newest
        L.tail = newest
        L.size = L.size + 1

    def remove_first(self, L):
        if L.head is None:
            raise Empty('list is empty')
        L.head = L.head.next
        L.size = L.size - 1