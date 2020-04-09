# has push / pop methods
# S.push(e) - add element e to the top of the stack
# S.pop() - remove and return the top element from the stack and raise error if empty
# convenience methods
# S.top() - return a ref to the top element of the stack without removing it and raise error if empty (aka peek)
# S.is_empty() - return true if stack is empty
# len(S) - use __len__ to return the number of elements in the stack

# Q.enqueue(e) - add element to the back of queue
# Q.dequeue() - remove and return the first element from queue if its not empty


class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass


class Queue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * Queue.DEFAULT_CAPACITY # create an empty queue
        self._size = 0
        self._front = 0

    def enqueue(self, e):
        """add an elem to the back (tail) of the queue"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))

        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def dequeue(self):
        """remove and return the first element (head)"""
        if self.is_empty():
            raise Empty('queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None  # optional
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1

        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)

        return answer

    def _resize(self, new_cap):
        old = self._data
        self._data = None * new_cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0  # realign

    def is_empty(self):
        """return true if stack is empty"""
        return self._size == 0

    def __len__(self):
        return self._size

    def first(self):
        if self.is_empty():
            raise Empty('queue is empty')
        return self._data[self._front]