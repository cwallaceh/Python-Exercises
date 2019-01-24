# Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.

# Analysis
# Because prefix are the first letters, let's keep track of every prefix, and compare them
# when the condition returns true, then we had found the longest common prefix.


def longest_common_prefix(arr):
    """O(k*n)"""
    n_s = len(arr)
    min_s = min(arr)

    prefix = []
    # Iterate through each characted
    for i in range(len(min_s)):
        # Iterate through each word - 1
        for j in range(n_s - 1):
            if arr[j][i] != arr[j + 1][i]:
                return ''.join(prefix)
        prefix.append(arr[j][i])
    return ''.join(prefix)


arr = ['hemistiquio', 'hemisferio', 'hemiciclo', 'hemiplejia']
print(longest_common_prefix(arr))
