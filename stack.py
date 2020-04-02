# has push / pop methods
# S.push(e) - add element e to the top of the stack
# S.pop() - remove and return the top element from the stack and raise error if empty
# convenience methods
# S.top() - return a ref to the top element of the stack without removing it and raise error if empty (aka peek)
# S.is_empty() - return true if stack is empty
# len(S) - use __len__ to return the number of elements in the stack


class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass


class Stack:
    def __init__(self):
        self._data = [] # create an empty stack

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.is_empty():
            raise Empty('stack is empty')

        return self._data.pop() # remove last elem from list

    def is_empty(self):
        """return true if stack is empty"""
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

    def top(self):
        if self.is_empty():
            raise Empty('stack is empty')
        return self._data[-1]