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
        self.__size = 0

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
        if self._elem.next is not None:
            self._elem = self._elem.next
        else:
            index = self._hash(self._elem.data)
            self._elem = None
            for i in range(index + 1, len(self._hashtable)):
                if self._hashtable[i] is not None:
                    self._elem = self._hashtable[i]
                    break
        return tmp.data

    def hash_function(self, key):
        return key % self.num_of_buckets

    def add(self, element):
        index = self._hash(element)
        if self._hashtable[index] is None:
            self._hashtable[index] = Node(element)
        else:
            n = Node(element, self._hashtable[index])
            self._hashtable[index] = n

    def remove(self, key=None):
        i = self.hash_function(key)
        if key in self.buckets[i]:
            self.buckets[i].remove(key)

    def contains(self, element):
        index = self._hash(element)
        n = self._hashtable[index]
        while (n != None):
            if (n.data == element):
                return True
            n = n.next
        return False

    def _hash(self, element):
        print(hash(element))
        return hash(element) % self._capacity

    def display(self):
        for e in self._hashtable:
            while e is not None:
                print(e.data)
                e = e.next


hset = HashSet(100)
hset.add(8)
hset.add(6)
hset.add(9)
hset.remove(6)
hset.display()
print("\n")
print(hset.contains(7))
print(hset.contains(9))
