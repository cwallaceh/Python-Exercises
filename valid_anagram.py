# Valid Anagram

# Given two strings s and t,
# write a function to determine if t is an anagram of s.

s = 'forty five'
t = 'over fifty'


def valid_anagram(s, t):
    """O(s+t)"""
    if len(s) != len(t):  # O(1)
        return False

    s_dict = {}
    t_dict = {}
    for char in s:  # O(len(s))
        if char in s_dict.keys():
            s_dict[char] += 1
        else:
            s_dict[char] = 1
    for char in t:  # O(len(t))
        if char in t_dict.keys():
            t_dict[char] += 1
        else:
            t_dict[char] = 1

    for key in s_dict.keys():  # O(n)
        if s_dict[key] != t_dict[key]:
            return False

    return True


print(valid_anagram(s, t))
