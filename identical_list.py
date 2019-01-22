# Given an list A of objects and another list B which is identical
# to A except that one element is removed, find that removed element.

# Identical should imply the same elements in the same order


def find_missing_element(A, B):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    for i in range(len(A) - 1):
        if A[i] != B[i]:
            return A[i]
    # If no element before is missing,
    # return the last one
    return A[-1]


A = [1, 2, 3, 4, 5]
B = [1, 2, 3, 5]
print(find_missing_element(A, B))
