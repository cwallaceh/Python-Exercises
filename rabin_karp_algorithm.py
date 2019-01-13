# Rabin-Karp Algorithm for Pattern Searching

# Given a text txt[0..n-1] and a pattern pat[0..m-1],
# write a function search(char pat[], char txt[])that prints all occurrences of pat[] in txt[].
# You may assume that n > m.

txt = "BACDGABCDABCD"
pat = "ABCD"


def rabin_karp(txt, pat):
    """O(n) complexity"""
    # Traverse the txt using a len(pat) window
    for new in [txt[i:i + len(pat)] for i in range(len(txt) - len(pat) + 1)]:
        # Check if the hash value is the same
        if hash(new) == hash(pat):
            print(new)


rabin_karp(txt, pat)
