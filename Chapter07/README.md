# Heaps and Priority Queues

## Heaps

A heap data structure is a specialization of a tree in which the nodes are ordered in a specific way. A Heap can be of two types:

- Max Heap
- Min Heap

In a **max heap**, each parent node value must always be greater than or equal to all its children. In this kind of tree, the root node must be the greatest value in the tree. In a **min heap**, the relationship between parent and children is that the value of the parent node must always be less than or equal to its children. This rule should be followed by all the nodes in the tree

If the binary heap is a complete binary tree with n nodes, then it will have a minimum height of log2n. In order to implement the heap, we can derive a relationship between parent and child nodes in index values. The relationship is that the children of any node at the n index can be retrieved easily, in other words, the left child will be located at 2n, and the right child will be located at 2n + 1
