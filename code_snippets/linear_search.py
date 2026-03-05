"""
Linear Search Implementation
Time Complexity: O(n)
"""

def linear_search(arr, key):
    for index, value in enumerate(arr):
        if value == key:
            return index
    return -1


def count_occurrences(arr, key):
    count = 0
    for value in arr:
        if value == key:
            count += 1
    return count


def run_example():
    numbers = [4, 2, 7, 2, 9, 2, 11]
    target = 2

    print("Array:", numbers)

    position = linear_search(numbers, target)

    if position != -1:
        print(f"First occurrence at index {position}")
    else:
        print("Element not found")

    total = count_occurrences(numbers, target)
    print(f"Total occurrences of {target}: {total}")


if __name__ == "__main__":
    run_example()
