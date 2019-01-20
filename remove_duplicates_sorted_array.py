# Given a sorted array, remove the duplicates in place such
# that each element appear only once and return the new length.
# Do not allocate extra space for another array,
# you must do this in place with constant memory O(1).

# For example, given input array A = [1,1,2],
# your function should return length = 2, and A is now [1,2].


def remove_duplicates_sorted(sorted_arr):
    """Remove duplicated elements from a sorted array, without using extra space
    Time complexity = O(n)
    Space complexity = O(1)
    """
    i = 0
    while i < len(sorted_arr) - 1:
        # If next value is the same as the current value
        if sorted_arr[i] == sorted_arr[i + 1]:
            # Pop from the array
            sorted_arr.pop(i)
        else:
            # Move to the next element
            i += 1
    print(sorted_arr)
    return len(sorted_arr)

# What if duplicates are allowed at most twice?
# For example, given sorted array A = [1,1,1,2,2,3],
# your function should return length = 5, and A is now [1,1,2,2,3].


def remove_duplicates_sorted_II(sorted_arr, allows):
    """Remove duplicated elements from a sorted array, without using extra space
    allows indicated the amount the number can be repeated before taking it out
    Time complexity = O(allows * n)
    Space complexity = O(1)
    """
    i = 0
    counter = 0
    while i < len(sorted_arr) - allows:
        # If next value is the same as the current value
        for j in range(1, allows + 1):
            if sorted_arr[i] == sorted_arr[i + j]:
                counter += 1
                if counter == allows:
                    # Pop element
                    sorted_arr.pop(i)
                    counter = 0
                    i -= 1
        # Move to the next element
        i += 1
        counter = 0
    print(sorted_arr)
    return len(sorted_arr)


arr = [1, 1, 2, 2, 3, 4, 5, 5, 6, 6, 7, 7, 8, 9]
print(remove_duplicates_sorted(arr))
arr = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5]
print(remove_duplicates_sorted_II(arr, 1))
