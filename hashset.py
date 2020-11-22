class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class HashSet:
    def __init__(self, capacity):
        self._hashtable = [None] * capacity
        self._capacity = capacity
        self.num_of_buckets = 20000
        self.buckets = [[] for i in range(self.num_of_buckets)]
        
    def levelOrderIterator(self):
        for i in range(self._size):
            isYield = False
            for e in self._hashtable:
                for j in range(i):
                    if (e != None):
                        e = e.next
                if (e != None):
                    yield e.data
                    isYield = True
            if (isYield == False):
                break

    def levelOrderIteratorWithQueue(self):
        yield None
        
    def __next__(self):
        if self._elem == None:
            raise StopIteration

        tmp = self._elem
        if (self._elem.next != None):
            self._elem = self._elem.next
        else:
            index = self._hash(self._elem.data)
            self._elem = None
            for i in range(index + 1, len(self._hashtable)):
                if (self._hashtable[i] != None):
                    self._elem = self._hashtable[i]
                    break
        return tmp.data

    def hash_function(self, key):
        return key % self.num_of_buckets

    def add(self, key=None):
        i = self.hash_function(key)
        if not key in self.buckets[i]:
            self.buckets[i].append(key)

    def remove(self, key=None):
        i = self.hash_function(key)
        if key in self.buckets[i]:
            self.buckets[i].remove(key)

    def contains(self, key=bool):
        i = self.hash_function(key)
        if key in self.buckets[i]:
            return True
        return False

    def _hash(self, element):
        print(hash(element))
        return hash(element) % self._capacity

    def display(self):
        for e in self._hashtable:
            while e is not None:
                print(e.data)
                e = e.next


HS = HashSet(100)
HS.add(8)
HS.add(6)
HS.add(9)
# print(HS.contains(7))
# print(HS.contains(9))
