# Heaps and Priority Queues

## Heaps

A heap data structure is a specialization of a tree in which the nodes are ordered in a specific way. A Heap can be of two types:

- Max Heap
- Min Heap

In a **max heap**, each parent node value must always be greater than or equal to all its children. In this kind of tree, the root node must be the greatest value in the tree. In a **min heap**, the relationship between parent and children is that the value of the parent node must always be less than or equal to its children. This rule should be followed by all the nodes in the tree

If the binary heap is a complete binary tree with n nodes, then it will have a minimum height of log2n. In order to implement the heap, we can derive a relationship between parent and child nodes in index values. The relationship is that the children of any node at the n index can be retrieved easily, in other words, the left child will be located at 2n, and the right child will be located at 2n + 1. Index should start from 1, not 0.

### Implementing a Min Heap

```python
class MinHeap:
  def __init__(self):
    self.heap = [0]
    self.size = 0
```

In the above code, we have created a class named `MinHeap` and initialized the heap list with a single element 0. This is done to make the index start from 1. We have also initialized the size of the heap to 0.

#### Inserting an Element

We first append (insert it in the last position) the element to the heap list and increment the size of the heap. Then we call the `heapify` method to maintain the heap property. Heapifying is the process of maintaining the heap property by rearranging the elements in the heap.
We need a helper method to swap the elements in the heap list.

```python
def arrange(self, k):
  while k // 2 > 0: # while parent exists
    if self.heap[k] < self.heap[k // 2]:
      self.heap[k], self.heap[k // 2] = self.heap[k // 2], self.heap[k]
    k //= 2

def insert(self, item):
  self.heap.append(item)
  self.size += 1
  self.arrange(self.size)
```
