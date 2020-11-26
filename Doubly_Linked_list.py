class Node:
    def __init__(self, data=None, prev=None, next=None, size = 0):
        self.data = data
        self.prev = prev
        self.next = next
        self.size = size

    def __repr__(self):
        return repr(self.data)


class DoubleLinkedList(Node):
    def __init__(self):
        super().__init__()
        self.data = None
        self.next = None
        self.head = None

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
class Node:
    def __init__(self, data=None, prev=None, next=None, size=0):
        self.data = data
        self.prev = prev
        self.next = next
        self.size = size

    def __repr__(self):
        return repr(self.data)


class DoublyLinkedList:
    def __init__(self):
        self.data = None
        self.head = None
        self.tail = None
        self.count = 0
        self.size = None

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return str(nodes)

    def iter(self):
        current = self.head
        while current:
            value = current.data
            current = current.next
            yield value

    def display(self):
        for node in self.iter():
            print(node, end=' -> ')

    def add(self, data):
        new_item = Node(data, None, None)
        if self.head is None:
            self.head = new_item
            self.tail = self.head
        else:
            new_item.prev = self.tail
            self.tail.next = new_item
            self.tail = new_item

        self.count += 1

    def remove(self, key):
        node = self.head
        while node:
            if node.data == key and node == self.head:
                if not node.next:
                    node = None
                    self.head = None
                    return
                else:
                    nxt = node.next
                    node.next = None
                    nxt.prev = None
                    node = None
                    self.head = nxt
                    return
            elif node.data == key:
                if node.next:
                    nxt = node.next
                    prev = node.prev
                    prev.next = nxt
                    nxt.prev = prev
                    node = None
                    node.next = None
                    node.prev = None
                    return
                else:
                    prev = node.prev
                    prev.next = None
                    node.prev = None
                    node = None
                    return
            node = node.next


dll = DoublyLinkedList()
dll.add(4)
dll.add(9)
dll.add(90)
dll.add(45)
dll.remove(4)
dll.display()
