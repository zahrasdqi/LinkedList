import SinglyLinkedList

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def make_doubly(self, Singlylinkedlist):
        current_node = Singlylinkedlist.head
        while current_node:
            self.append(current_node.data)
            current_node = current_node.next

    def shift(self, num):
        current_node = self.head
        for _ in range(num):
            current_node = current_node.next
        self.head = current_node
        current_node.prev = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


SLinkedList=SinglyLinkedList()
SLinkedList.append(1)
SLinkedList.append(2)
SLinkedList.append(3)

DLinkedList=DoublyLinkedList()
DLinkedList.make_doubly(SLinkedList)
DLinkedList.print_list()
DLinkedList.shift(2)
DLinkedList.print_list()

