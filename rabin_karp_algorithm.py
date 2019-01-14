# Rabin-Karp Algorithm for Pattern Searching using a simple Hash Table

# Given a text txt[0..n-1] and a pattern pat[0..m-1],
# write a function search(char pat[], char txt[])that prints all occurrences of pat[] in txt[].
# You may assume that n > m.


txt = "BACDGABCDABCD"
pat = "ABCD"

# d is the number of characters in the input alphabet
d = 256


class HashTable():

    def __init__(self, n=10):
        self.hash_table = self.create_hash_table(n)

    def create_hash_table(self, n):
        """Function to create hash table with 'n' values"""
        hash_table = [[] for _ in range(n)]
        return hash_table

    def hashing_func(self, key):
        return hash(key) % len(self.hash_table)


def rabin_karp(txt, pat, d):
    """O(n) complexity"""
    # Traverse the txt using a len(pat) window

    _hash_ = HashTable(d)
    for new in [txt[i:i + len(pat)] for i in range(len(txt) - len(pat) + 1)]:
        # Check if the hash value is the same
        if _hash_.hashing_func(new) == _hash_.hashing_func(pat):
            print(new)


rabin_karp(txt, pat, d)
