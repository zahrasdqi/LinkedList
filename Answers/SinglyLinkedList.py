class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
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



    def insert_in_front(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def insert_in_back(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node


    def delete_at_front(self):
        if self.head is None:
            return None

        deleted_data = self.head.data
        self.head = self.head.next

        return deleted_data


    def delete_at_back(self):
        if self.head is None:
            return None
        if self.head.next is None:
            deleted_data = self.head.data
            self.head = None
            return deleted_data
        current = self.head
        while current.next.next:
            current = current.next
        deleted_data = current.next.data
        current.next = None
        return deleted_data


    def search(self,number):
        current = self.head
        while current:
            if current.data == number:
                return True
            current = current.next
        return False


    def clear(self):
        self.head = None


    def size(self):
        list_size=self.size
        return list_size
    

    def print_forward(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
        

    #def print_backward(self):
        


    def reverse_recursive(self):
        def reverse(current, prev):
            if current is None:
                self.head = prev
                return
            next_node = current.next
            current.next = prev
            reverse(next_node, current)

        if self.head is None:
            return
        reverse(self.head, None)


    #def reverse_non_recursive(self):

SinglyLinkedList=SinglyLinkedList()
SinglyLinkedList.append(1)
SinglyLinkedList.append(2)
SinglyLinkedList.insert_in_front(1)
SinglyLinkedList.insert_in_back(2)
SinglyLinkedList.delete_at_front()
SinglyLinkedList.delete_at_back()
print(SinglyLinkedList.search(2))
SinglyLinkedList.print_forward()
print(SinglyLinkedList.size())
print(SinglyLinkedList.clear())




    




