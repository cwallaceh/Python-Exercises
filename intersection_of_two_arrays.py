# Intersection of Two Arrays

# Given two arrays, write a function to compute their intersection.


arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 3, 4, 5, 6, 7]


def intersection(arr1, arr2):
    """Using a Hash Map
    Time Complexity: O(m + n)
    Space Complexity: O(2n)
    """
    intersection = {}
    elements = []
    for element in arr1:
        if element not in intersection.keys():
            intersection[element] = 1

    for element in arr2:
        if element in intersection.keys() and element not in elements:
            elements.append(element)

    return elements


print(intersection(arr1, arr2))
