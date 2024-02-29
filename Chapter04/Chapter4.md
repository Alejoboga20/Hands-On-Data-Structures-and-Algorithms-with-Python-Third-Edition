# Linked Lists

A linked list is a linear data structure where each element is a separate object. Each element (we will call it a node) of a list is comprising of two items - the data and a reference to the next node. The last node has a reference to null. The entry point into a linked list is called the head of the list. It should be noted that the head is not a separate node, but the reference to the first node. If the list is empty then the head is a null reference.

A linked list is a dynamic data structure. The number of nodes in a list is not fixed and can grow and shrink on demand. Any application which has to deal with an unknown number of objects will need to use a linked list.

One disadvantage of a linked list against an array is that it does not allow direct access to the individual elements. If you want to access a particular item then you have to start at the head and follow the references until you get to that item.

An advantage of a linked list is that elements can be inserted into the list without reallocation or reorganization of the entire structure because the data items need not be stored contiguously in memory or on disk.

## Singly linked lists

A linked list (also called a singly linked list) contains a number of nodes in which each node contains data and a pointer that links to the next node. The link of the last node in the list is None, which indicates the end of the list

Traversal of the linked lists means visiting all the nodes of the list, from the starting node to the last node. A singly linked list can be created using a simple class to hold the list.

```python
class SinglyLinkedList:
    def __init__ (self):
        self.head = None
```

### Inserting a node in a singly linked list

We can append items to the list.

```python
class SinglyLinkedList:
    def __init__ (self):
        self.head = None
        self.size = 0

def append(self, data):
    # Encapsulate the data in a Node
    node = Node(data)
    # If the list is empty, then the new node is the head of the list
    if self.head is None:
        self.head = node
    # Otherwise, find the last node and append the new node
    else:
        current = self.head
        while current.next:
            current = current.next
        current.next = node
```

In this, we have to traverse the entire list to find the insertion point. This may not be a problem when there are just a few items in the list, but it will be very inefficient when the list is long, as it will have to traverse the whole list to add an item every time.

```python
class SinglyLinkedList:
    def __init__ (self):
        self.tail = None
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
```

This implementation reduces the time complexity of the append operation from O(n) to O(1).

### Appending items at intermediate positions

To append or insert an element in an existing linked list at a given position, firstly, we have to traverse the list to reach the desired position where we want to insert an element. An element can be inserted in between two successive nodes using two pointers (prev and current).

```python
class SinglyLinkedList:
    def __init__ (self):
        self.tail = None
        self.head = None
        self.size = 0

    def append_at_a_location(self, data, index):
        current = self.head
        prev = self.head
        node = Node(data)
        count = 1

        while current:
            if index == 1:
                node.next = current
                self.head = node
                print(count)
                return
            elif count == index:
                node.next = current
                prev.next = node
                return
            count += 1
            prev = current
            current = current.next
        if count < index:
            print("The list has less number of elements")
```

### Querying a singly linked list

To query a singly linked list, we have to traverse the list from the head to the last node. We can use a while loop to traverse the list and print the data of each node.

```python
def search(self, data):
    for node in self.iter():
        if data == node:
            return True
    return False
```

### Deleting a node from a singly linked list

To Delete the first node from a singly linked list, we have to change the head of the list to the next node. The first node will be removed from the list and the second node will become the head of the list.

```bash
1. A temporary pointer (current pointer) is created that points to the first node (head node) of the list.
2. The current pointer is moved to the next node.
```

To Delete the last node from a singly linked list, we have to traverse the list to reach the last node. We have to keep track of the previous node of the last node. The next pointer of the previous node is set to None, which indicates the end of the list.

To delete any intermediary node, we need two pointers similar to the case when we learned to delete the last node; in other words, the current pointer and the prev pointer. Once we reach the node that is to be deleted, the desired node can be deleted by making the previous node point to the next node of the node that is to be deleted.
