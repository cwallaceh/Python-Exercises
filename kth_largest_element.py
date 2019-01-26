# Kth Largest Element in an Array

# Find the kth largest element in an unsorted array.
# Note that it is the kth largest element in the sorted order

# For example, given [3,2,1,5,6,4] and k = 2, return 5.

arr = [3, 2, 1, 5, 6, 4]
k = 2


def kth_largest_element(arr, k):
    """O(nlogn)"""
    arr.sort()
    return arr[-k]


print(kth_largest_element(arr, k))
