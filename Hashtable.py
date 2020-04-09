from linkedList_singular import LinkedList

class Hashtable0:

    def __init__(self, data):
        self._data = data

    def getHashCodeKey(self):
        return 1

    def convertToIndex(self, hashcode):
        return hashcode // 2

    def put(self, key, value):
        hashcode = self.getHashCodeKey()
        index = self.convertToIndex(hashcode)

        # java specific implementation of LL
        # list = LinkedList(self._data[index])
        # list.insert(key, value)

        pass

    def get(self):
        pass

# LinkedList
# Hashtable(LinkedList)


INITIAL_CAPACITY = 50


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self):
        self.capacity = INITIAL_CAPACITY
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash(self, key):
        hashsum = 0

        # for each char in the key
        for idx, c in enumerate(key):
            # add (index + length of key) ^ (current char code)
            hashsum += (idx + len(key)) ** ord(c)

            # perform modulus to keep hashsum in range [0, self.capacity - 1]
            hashsum = hashsum % self.capacity
        return hashsum

myHashTable = HashTable
print(myHashTable.hash("eva"))