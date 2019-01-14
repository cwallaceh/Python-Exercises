import random

from timing import timing

array = random.sample(range(1, 1000), 999)


def merge_sort(array):
    """O(n log n)"""
    n = len(array)
    # Divide the array in half
    if n > 1:
        i = n // 2
        left = array[:i]
        right = array[i:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Copy data to temp arrays
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

    return array


timing(merge_sort)(array)
