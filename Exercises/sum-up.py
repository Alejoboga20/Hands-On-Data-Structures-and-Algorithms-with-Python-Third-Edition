# def sum_up(numbers: list[int], target: int) -> list[int]:
#     indices = []

#     for index, number in enumerate(numbers):
#         i = index
#         if number >= target:
#             print(f"Number {number} is greater than target {target}")
#             continue

#         while i < len(numbers) - 1:
#             if number + numbers[i + 1] == target:
#                 print(f"Number {number} + {numbers[i + 1]} = {target}")
#                 indices.append(index)
#                 indices.append(i + 1)
#                 return indices
#             i += 1

#     return []


# numbers = [1, 2, 3, 12, 21, 35, 2, 3, 6, 6, 421, 20, 2346, 23]
# print(sum_up(numbers, 23))


def sum_ap(numbers: list[int], target: int) -> list[int]:
    # Using a dictionary to map number values to their indices
    num_dict = {}

    for index, number in enumerate(numbers):
        complement = target - number
        if complement in num_dict:
            # Found the pair that sums to target
            return [num_dict[complement], index]
        num_dict[number] = index

    return []


# Example usage
numbers = [1, 2, 3, 12, 21, 35, 2, 3, 6, 6, 421, 20, 2346, 23]
print(sum_ap(numbers, 23))
