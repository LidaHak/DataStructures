class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class List:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head

    def add(self, data):
        temp_node = Node(data)
        if self.head.data is None:
            self.head = temp_node
            self.tail = temp_node
            temp_node.next = self.head
        else:
            self.tail.next = temp_node
            self.tail = temp_node
            self.tail.next = self.head

    def Min(self):
        current = self.head
        min_value = self.head.data
        if self.head is None:
            print("Empty list!")
        else:
            while True:
                if min_value > current.data:
                    min_value = current.data
                current = current.next
                if current == self.head:
                    break
        print("The min_value value in the list: " + str(min_value))

    def Max(self):
        current = self.head
        max_value = self.head.data
        if self.head is None:
            print("Empty list!")
        else:
            while True:
                if max_value < current.data:
                    max_value = current.data
                current = current.next
                if current == self.head:
                    break
        print("The max_value value in the list: " + str(max_value))


class Circular_Linked_List:
    cll = List()
    cll.add(4)
    cll.add(78)
    cll.add(22)
    cll.Min()
    cll.Max()
