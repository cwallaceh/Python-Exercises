import random

from timing import timing

array = random.sample(range(1, 1000), 999)


def selection_sort(array):
    """
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    n = len(array)
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if array[min_idx] > array[j]:
                min_idx = j
        # Swap
        array[i], array[min_idx] = array[min_idx], array[i]

    return array


timing(selection_sort)(array)
