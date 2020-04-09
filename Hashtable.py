from linkedList_singular import LinkedList

# class Hashtable0:
#
#     def __init__(self, data):
#         self._data = data
#
#     def getHashCodeKey(self):
#         return 1
#
#     def convertToIndex(self, hashcode):
#         return hashcode // 2
#
#     def put(self, key, value):
#         hashcode = self.getHashCodeKey()
#         index = self.convertToIndex(hashcode)
#
#         # java specific implementation of LL
#         # list = LinkedList(self._data[index])
#         # list.insert(key, value)
#
#         pass
#
#     def get(self):
#         pass
#
# # LinkedList
# # Hashtable(LinkedList)

# from LL_node import Node

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
            myKeycode = ord(c)
            myLen = len(key)
            hashsum += (idx + len(key)) ** ord(c)

            # perform modulus to keep hashsum in range [0, self.capacity - 1]
            hashsum = hashsum % self.capacity

            myHS = hashsum
        return hashsum

    def insert(self, key, value):
        self.size += 1
        index = self.hash(key)
        node = self.buckets[index]

        #no collision, so just add a new node at loc. Its .next val is None
        if node is None:
            self.buckets[index] = Node(key, value)
            return

        #have a collision, iterate to the end of the linked list and add new node there
        prev = node
        while node is not None:
            prev = node
            node = node.next

        prev.next = Node(key, value)  # found the empty spot, create node there

    def find(self, key):
        index = self.hash(key)
        node = self.buckets[index]

        # either already found the right node or go through the linked list there
        while node is not None and node.key != key:
            node = node.next

        if node is None:  # not found
            return None
        else:
            return node.value

    def remove(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        prev = None

        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:  # not found
            return None
        else:
            self.size -= 1
            result = node.value

            # del the element in the linked list
            if prev is None:
                node = None  # only 1 item in LL, so just del
            else:
                prev.next = prev.next.next

            return result


myHashTable = HashTable()
# print(myHashTable.hash("eva"))
print(myHashTable.hash("a"))
print(myHashTable.hash("aa"))
print(myHashTable.hash("abc"))