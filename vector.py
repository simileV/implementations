

# https://www.geeksforgeeks.org/implementation-of-dynamic-array-in-python/

class Vector():
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.arr = [0] * 1

    def size(self):
        return self.size

    def capacity(self):
        return self.capacity

    def is_empty(self):
        if self.capacity == 0:
            return True
        return False

    def at(self, index):
        if index < 0 or index >= self.size:
            return IndexError("index is out of bounds")
        return self.arr[index]

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

        if self.size + 1 > self.capacity():
            self.resize(self.capacity * 2)

        temp = self.arr[index]
        self.arr[index] = item

        # range(start, stop, step)
        # for i in range(self.capacity, index - 1, -1):
        for i in range(self.capacity, index, -1):
            self.arr[i + 1] = self.arr[i]

    def insert(self, item):
        self.insert(0, item)

    def pop(self):
        pass

    def delete(self, index):
        pass

    def remove(self):
        pass

    def find(self, item):
        pass

# new raw data array

#size() - number of items




thislist = ["apple", "banana", "cherry"]
thislist.append("test")




print(thislist)