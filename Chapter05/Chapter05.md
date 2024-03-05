# Stacks and Queues

## Stacks

A stack is a collection of objects that are inserted and removed according to the last-in, first-out (LIFO) principle. Stacks stores data in a specific order similar to arrays or linked lists with some constraints.

- **Push**: Add an element only to the top of a stack
- **Pop**: Remove an element only from the top of a stack
- **Peek**: Get the top element of the stack without removing it

The operations in a stack are performed through a pointer named `top`.
Stacks can be implemented using arrays or linked lists. The array implementation is simple and easy to implement, but it has a fixed size. The linked list implementation is dynamic and can grow or shrink as needed, but it requires more memory and time to manage the pointers.

## Queues

A queue is a collection of objects that are inserted and removed according to the first-in, first-out (FIFO) principle. Queues stores data in a specific order similar to arrays or linked lists with some constraints.

In python we can use the `deque` class from the `collections` module to implement a queue. The `deque` class is a double-ended queue that supports adding and removing elements from either end in O(1) time.

We can also implemente a queue using a list, a linked list or a stack. The list implementation is simple and easy to implement, but it has a fixed size. The linked list implementation is dynamic and can grow or shrink as needed, but it requires more memory and time to manage the pointers. The stack implementation is not efficient.
