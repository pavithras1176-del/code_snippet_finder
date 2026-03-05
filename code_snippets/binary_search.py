"""
Binary Search Algorithm
Time Complexity: O(log n)
Space Complexity: O(1)
"""

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def validate_sorted(arr):
    """Ensure array is sorted before binary search"""
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def print_array(arr):
    print("Array elements:")
    for i in arr:
        print(i, end=" ")
    print()


def run_demo():
    numbers = [5, 8, 12, 16, 23, 38, 56, 72, 91]
    target = 23

    print_array(numbers)

    if not validate_sorted(numbers):
        print("Array must be sorted.")
        return

    index = binary_search(numbers, target)

    if index != -1:
        print(f"Element {target} found at index {index}")
    else:
        print("Element not found")


if __name__ == "__main__":
    run_demo()
