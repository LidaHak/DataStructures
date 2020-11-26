class Node:
    def __init__(self, data, node):
        self.data = data
        self.next = None
        self.prev = None
        self.size = None



class Linked_List:
    def __init__(self, value):
        self.value = value
        self.head = None
        self.temp = None

    def display(self):
        values = self.head
        if values is None:
            print("Empty List!")
            return False

        while values:
            print(values.data, end=" -> ")
            values = values.next

    def size(self):
        current = self.head
        length = 0
        while current:
            length = length + 1
            current = current.next
        return length

    def add(self, data):
        new_node = Node(data, node='')
        if self.head is None:
            self.head = new_node
            return
        the_last_one = self.head
        while the_last_one.next:
            the_last_one = the_last_one.next
        the_last_one.next = new_node

    def remove_from_beginning(self):
        if self.head == None:
            print('The list is empty!')
        if self.head == None:
            return None
        else:
            self.head = self.head.next

    def remove_from_end(self):
        if self.head == None:
            return None
        if self.head.next == None:
            return None
        temp = self.head
        while (temp.next.next):
            temp = temp.next
        temp.next = None
        return self.head

    def remove_from_specific_position(self):
        position = int(input("Please, enter the position you want to delete: "))
        i = 1
        temp = self.head
        while i < position - 1:
            temp = temp.next
            i += 1
        self.next = temp.next
        temp.next = self.next.next
        self.next = None

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next  # the 'next' in this line is just a local variable
        self.head = prev



our_list = Linked_List(value='')
our_list.head = Node(1, node=0)
our_list.add(6)
our_list.add(7)
our_list.add(10)
our_list.add(90)
our_list.add(45)
# our_list.remove_from_beginning()
# our_list.remove_from_end()
# our_list.remove_from_specific_position()
our_list.display()
print("The reverse list is: " + str(our_list.reverse()))
print("\n")
print("The length of the list is " + str(our_list.size()))
