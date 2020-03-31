

# https://www.geeksforgeeks.org/implementation-of-dynamic-array-in-python/

class Vector():
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._arr = [None] * self._capacity

    def is_empty(self):
        if self._capacity == 0:
            return True
        return False

    def at(self, index):
        if index < 0 or index >= self._n:
            return IndexError("index is out of bounds")
        return self._arr[index]

    def resize(self, new_capacity):
        biggerArray = [0] * new_capacity

        for i in range(self._n):
            biggerArray[i] = self._arr[i]

        self._arr = biggerArray
        self._capacity = new_capacity

    def push(self, item):
        if self._n == self._capacity:
            self.resize(self._capacity * 2)

        self._arr[self._n] = item
        self._n += 1

    def insert(self, index, item):
        if index < 0 or index >= self._n:
            return IndexError("index is out of bounds")

        if self._n == self._capacity:
            self.resize(self._capacity * 2)

        # range(start, stop, step)
        # for i in range(self._capacity, index - 1, -1):
        for i in range(self._n, index, -1):
            self._arr[i] = self._arr[i-1]

        self._arr[index] = item
        self._n += 1

    def prepend(self, item):
        """add an element to the beginning of the list."""
        self.insert(0, item)

    def removeBookGoodrich(self, value):
        """remove first occurence of value or raise ValueError"""
        for i in range(self._n):
            if self._arr[i] == value: # found a match
                for j in range(i, self._n - 1): #shift others to fill gap
                    self._arr[j] = self._arr[j+1]
                self._arr[self._n - 1] = None
                self._n -= 1

                if self._n == (self._capacity / 4):
                    self.resize(self._capacity / 2)
                    
                return
        raise ValueError('value not found') # no match

    def pop(self):
        self._arr[-1] = None

        if self._n == (self._capacity / 4):
            self.resize(self._capacity / 2)

    def delete(self, index):
        """delete item at index, shifting all trailing elements left"""
        if index < 0 or index >= self._n:
            return IndexError("index is out of bounds")

        self._arr[index] = None

        for i in range(index, self._capacity):
            self._arr[i] = self._arr[i + 1]

    def remove(self, item):
        idxToDel = -1
        for i in range(self._n):
            if item == self._arr[i]:
                idxToDel = i

        self.delete(idxToDel)

    def find(self, item):
        foundIdx = -1

        for i in range(self._n):
            if item == self._arr[i]:
                return i
        return foundIdx

# new raw data array

#_n() - number of items




thislist = ["apple", "banana", "cherry"]
thislist.append("test")




print(thislist)