# Shortest Word Distance

# Given a list of words and two words word1 and word2
# return the shortest distance between these two words in the list.

# Example:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
# Given word1 = “coding”, word2 = “practice”, return 3.
# Given word1 = "makes", word2 = "coding", return 1.

words = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "coding"
word2 = "practice"


def shortest_word_distance(words, word1, word2):
    """First approach"""
    for idx, word in enumerate(words):
        if word == word1:
            index1 = idx
        elif word == word2:
            index2 = idx
    return abs(index2 - index1)


class shortestWord():
    """Using Hash table for repeated use"""

    def __init__(self, words):
        self.hash = {}
        for idx, word in enumerate(words):
            self.hash[word] = idx

    def distance(self, word1, word2):
        return abs(self.hash[word2] - self.hash[word1])


print(shortest_word_distance(words, word1, word2))
sh = shortestWord(words)
print(sh.distance(word1, word2))
