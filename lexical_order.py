# Return TRUE when the word is sorted in lexographic order as in ordering


word = "cat"
ordering = ['c', 'b', 'a', 't']


def check_ordering(word, ordering):
    """Recursive approach O(len(ordering))"""
    # Base cases
    if not word:
        return True
    # Recursion
    else:
        letter = word.pop(0)
        print(letter)
        for char in ordering:
            if letter == char:
                index = ordering.index(char)
                print(ordering[index:])
                return check_ordering(word, ordering[index:])
        return False


print(check_ordering(list(word), ordering))


# c
# ['c', 'b', 'a', 't']
# a
# ['a', 't']
# t
# ['t']
# True
# [Finished in 1.1s]
