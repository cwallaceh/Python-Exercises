# Binary search and linear search

from timing import timing


def binary_search(sorted_arr, search):
    """O(log n)"""
    n = len(sorted_arr)
    # Split arr
    if n >= 1:
        mid = n // 2
        if sorted_arr[mid] == search:
            return True
        elif sorted_arr[mid] < search:
            return binary_search(sorted_arr[mid + 1:], search)
        else:
            return binary_search(sorted_arr[:mid], search)
    else:
        return False


def linear_search(sorted_arr, search):
    """O(n)"""
    for element in sorted_arr:
        if element == search:
            return True
    return False


sorted_arr = range(0, 1000)
search = 999
print(timing(linear_search)(sorted_arr, search))
print(timing(binary_search)(sorted_arr, search))
