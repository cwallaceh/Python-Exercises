# There are N children standing in a line. Each child is assigned a rating value.
# You are giving candies to these children subjected to the following requirements:

# 1. Each child must have at least one candy.
# 2. Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?

# Example:
# children = [9, 6, 8, 1, 0, 2]
# candy = [2, 1, 3, 2, 1, 2]
# total_candy = 11

# Example:
# children = [0, 0.1, 0.2, 0.3, 0.4, 0.5]
# candy = [1, 2, 3, 4, 5, 6]
# total_candy = 21

import sys


def children_candy(children):
    """O(n^2)"""
    candy = [1] * len(children)
    # Find the min element
    min_ = [0, sys.maxsize]
    for idx, val in enumerate(children):
        if val < min_[1]:
            min_ = [idx, val]
    print(min_)
    # Assign candy from min index
    # Left
    print(candy)
    for i in range(min_[0], -1, -1):
        if children[i - 1] > children[i]:
            candy[i - 1] = candy[i] + 1
        print(candy)
    # Right
    for i in range(min_[0], len(children) - 1):
        if children[i + 1] > children[i]:
            candy[i + 1] = candy[i] + 1
        print(candy)
    print(candy)
    return sum(candy)


children = [9, 6, 8, 1, 0, 2]
print(children_candy(children))

# chidlren = [9, 6, 8, 1, 0, 2]
# candy = [1, 1, 1, 1, 1, 1]
# Right
# candy = [1, 1, 1, 1, 1, 2]
# Left
# candy = [1, 1, 1, 2, 1, 2]
# candy = [1, 1, 3, 2, 1, 2]
# candy = [1, 1, 3, 2, 1, 2]
# candy = [2, 1, 3, 2, 1, 2]
