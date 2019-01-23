# Given a non-empty array of integers, return the k most frequent elements.

arr = ['d', 'e', 'a', 'e', 'a', 'a', 'b', 'b', 'a', 'b', 'c', 'c', 'e', 'e', 'e']


def top_k_frequent_elements(arr, k):
    """
    """
    # Dictionary
    frequency = {}
    for element in arr:  # O(n)
        if element in frequency.keys():
            frequency[element] += 1
        else:
            frequency[element] = 1
    # Convert dict to a list of tuples
    rd = [(v, k) for k, v in frequency.items()]
    # Sort, reverse and return k elements
    rd.sort()
    rd = rd[::-1]
    top_k = [x[1] for x in rd[:k]]

    return top_k


print(top_k_frequent_elements(arr, 3))
