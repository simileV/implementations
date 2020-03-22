

# https://www.geeksforgeeks.org/implementation-of-dynamic-array-in-python/

class Vector():
    def __init__(self):
        self.size = 0
        self.capacity = 1
        # self.arr = [0] * 1
        self.arr = [None] * self.capacity

    def is_empty(self):
        if self.capacity == 0:
            return True
        return False

    def at(self, index):
        if index < 0 or index >= self.size:
            return IndexError("index is out of bounds")
        return self.arr[index]

    # def resize(self, new_capacity):
    #     biggerArray = [0] * new_capacity
    #
    #     for i in range(self.size):
    #         biggerArray[i] = self.arr[i]
    #
    #     self.arr = biggerArray
    #     self.capacity = new_capacity

    def resize(self, new_capacity):
        biggerArray = [0] * new_capacity

        for i in range(self.size):
            biggerArray[i] = self.arr[i]

        self.arr = biggerArray
        self.capacity = new_capacity

    def push(self, item):
        if self.size == self.capacity:
            self.resize(self.capacity * 2)

        self.arr[self.size] = item
        self.size += 1

    def insert(self, index, item):
        if index < 0 or index >= self.size:
            return IndexError("index is out of bounds")

        if self.size + 1 >= self.capacity:
            self.resize(self.capacity * 2)

        temp = self.arr[index]
        self.arr[index] = item

        # range(start, stop, step)
        # for i in range(self.capacity, index - 1, -1):
        for i in range(self.capacity, index, -1):
            self.arr[i + 1] = self.arr[i]

    def prepend(self, item):
        """add an element to the beginning of the list."""
        self.insert(0, item)

    def pop(self):
        self.arr[-1] = None

        if self.size == (self.capacity / 4):
            self.resize(self.capacity / 2)

    def delete(self, index):
        """delete item at index, shifting all trailing elements left"""
        if index < 0 or index >= self.size:
            return IndexError("index is out of bounds")

        self.arr[index] = None

        for i in range(index, self.capacity):
            self.arr[i] = self.arr[i + 1]

    def remove(self, item):
        idxToDel = -1
        for i in range(self.size):
            if item == self.arr[i]:
                idxToDel = i

        self.delete(idxToDel)

    def find(self, item):
        foundIdx = -1

        for i in range(self.size):
            if item == self.arr[i]:
                return i
        return foundIdx

# new raw data array

#size() - number of items




thislist = ["apple", "banana", "cherry"]
thislist.append("test")




print(thislist)