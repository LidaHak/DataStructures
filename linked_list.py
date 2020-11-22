class Node:
    def __init__(self, data, node):
        self.data = data
        self.next = None
        self.prev = None
        self.size = None


class Linked_List:
    def __init__(self):
        self.head = ""
        self.tail = ""

    # prints the values
    def display(self):
        values = self.head
        if values is None:
            print("Empty List!")
            return False

        while values:
            print(str(values.data))
            values = values.next

    def size(self):
        current = self.head
        length = 0
        while current:
            length = length + 1
            current = current.next
        return length

    # adds values to our list
    def add(self, data):
        new_node = Node(data, node='')
        if self.head is None:
            self.head = new_node
            return
        the_last_one = self.head
        while the_last_one.next:
            the_last_one = the_last_one.next
        the_last_one.next = new_node

    def remove_first(self):
        if self.head is not None:
            self.head = self.head.next

    def remove(self, data):
        if self.head.data == data:
            self.head = self.head.next
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    node.next = node.next.next

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


our_list = Linked_List()
our_list.head = Node(1, node=0)
#our_list.tail = Node(9, node=0)
our_list.add(6)
our_list.add(7)
our_list.add(10)
#our_list.remove(10)
# our_list.remove_first()
# our_list.remove_last()

our_list.display()
#our_list.size()
print("The length of the list is " + str(our_list.size()))
