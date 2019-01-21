import random

from timing import timing

array = random.sample(range(1, 1000), 999)


def bubble_sort(array):
    """
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    n = len(array)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n - i - 1
            if array[j] > array[j + 1]:
                # Swap
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


timing(bubble_sort)(array)
