from linkedList_doubly import LinkedList_doubly, Empty

"""doubly linked list with a double ended queue (deque)"""

class LinkedDeque(LinkedList_doubly):
    def first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._header._next._element  # get item just after header

    def last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._trailer._prev._element  # get item just before trailer

    def insert_first(self, e):
        self.insert_between(e, self._header, self._header._next)  # after header

    def insert_last(self, e):
        self.insert_between(e, self._trailer._prev, self._trailer)  # before trailer

    def delete_first(self):
        """remove the first element (after the header)"""
        if self.is_empty():
            raise Empty('Deque is empty')
        return self.delete_node(self._header._next)

    def delete_last(self):
        """remove the first element (after the header)"""
        if self.is_empty():
            raise Empty('Deque is empty')
        return self.delete_node(self._trailer._prev)