# Sorting

Sorting is a common task in programming. It is the process of arranging items in a list in a specific order. Sorting can be done in ascending or descending order. There are many sorting algorithms available, each with its own advantages and disadvantages. Some of the most common sorting algorithms are:

## Bubble Sort Algorithm

Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the
list is repeated until no swaps are needed, which indicates that the list is sorted.
The proecess is repeated `n-1` times for a list of `n` elements.

```python
def swap_elements(arr, first_index, second_index):
    temp = arr[first_index]
    arr[first_index] = arr[second_index]
    arr[second_index] = temp
```

![alt text](image.png)

After the first pass, the largest element will be at the end of the list. After the second pass, the second largest element will be at the second last position, and so on. The process is repeated until the list is sorted.

```python
def bubble_sort(unordered_list):
    iteration_number = len(unordered_list) - 1

    for i in range(iteration_number, 0, -1): # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
        for j in range(i): # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 | 0, 1, 2, 3, 4, 5, 6, 7, 8 | 0, 1, 2, 3, 4, 5, 6, 7 | 0, 1, 2, 3, 4, 5, 6 | 0, 1, 2, 3, 4, 5 | 0, 1, 2, 3, 4 | 0, 1, 2, 3 | 0, 1, 2 | 0, 1
            if unordered_list[j] > unordered_list[j+1]:
                temp = unordered_list[j]
                unordered_list[j] = unordered_list[j+1]
                unordered_list[j+1] = temp
```

Time complexity of bubble sort is `O(n^2)`. Bubble sort is not recommended for large lists.
