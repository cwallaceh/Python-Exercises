# Given two words (start and end), and a dictionary, 
# find the length of shortest transformation sequence from start to end,
# such that only one letter can be changed at a time and each intermediate word must exist in the dictionary.

# start = "hit"
# end = "cog"
# arr = ["hot","dot","dog","lot","log"]


def check_diff(w1, w2, diff=1):
    """auxilar function to check if words are one letter appart"""
    counter = 0
    if len(w1) == len(w2):
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                if counter == diff:
                    return False
                counter += 1
        return True
    return False


def shortest_transformation(start, end, arr):
    """BFS appproach guarantees optimal answers"""

    queue = []
    queue.append(start)  # Add First Node
    visited_nodes = []

    while queue:
        print(queue)
        # Visit the first node
        node = queue.pop(0)
        visited_nodes.append(node)
        # Check if we reached the end
        if check_diff(node, end):
            print(visited_nodes)
            return True
        else:
            # Visit next node
            for element in arr:
                if element not in visited_nodes and element not in queue:
                    if check_diff(node, element):
                        queue.append(element)
    return False


start = "hit"
end = "cog"
arr = ["hot", "dot", "dog", "lot", "log", "hut"]
print(shortest_transformation(start, end, arr))
