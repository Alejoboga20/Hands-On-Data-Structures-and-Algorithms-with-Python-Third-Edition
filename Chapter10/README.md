# Searching

A search algorithm is a method for finding an item or group of items with specific properties within a collection of items. The items in the collection can be thought of as being stored in an array or list, and the process of searching for an item can be thought of as comparing the item with each item in the collection until a match is found.

The set of items can be already sorted or unsorted.

## Linear Search

Linear search is the simplest search algorithm. It is a brute-force search algorithm that compares each element in the list with the target element until a match is found. If the target element is found, the algorithm returns the index of the element in the list. If the target element is not found, the algorithm returns `None`.

### Unordered linear search

We match the target element with each element in the list until a match is found.

```python
def search(unordered_list, search_term):
  for i, item in enumerate(unordered_list):
    if search_term = item
      return i
  return None
```

The time complexity of this algorithm is `O(n)`, where n is the number of elements in the list.

### Ordered linear search
