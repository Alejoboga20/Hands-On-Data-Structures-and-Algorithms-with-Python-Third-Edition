"""
A Linked List is a collection of nodes that form a linear sequence.
Each node contains data and a reference (the link) to the next node in the sequence.

Types:
  - Singly Linked List
  - Doubly Linked List
  - Circular Linked List
"""

# Node class for a singly linked list


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


singly_linked_list = SinglyLinkedList()
singly_linked_list.append(1)
singly_linked_list.append(2)
singly_linked_list.append(3)

singly_linked_list.display()
