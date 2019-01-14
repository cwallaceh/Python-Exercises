# Check if a string is a valid palindrome

from timing import timing


@timing
def check_palindrome(str_):
    """Naive method, reverse string, compare O(2n)"""
    str_reversed = ''
    for i in range(len(str_) - 1, -1, -1):  # O(n)
        str_reversed += str_[i]

    for i in range(len(str_reversed) - 1):  # O(n)
        if str_reversed[i] != str_[i]:
            return False

    return True


@timing
def palindrome_pointers(str_):
    """Second method with pointers, O(n/2)"""
    i = 0
    j = len(str_) - 1

    for i in range(len(str_) / 2 - 1):
        if str_[i] != str_[j]:
            return False
        else:
            i += 1
            j -= 1

    return True


str_ = "ollo"
print(check_palindrome(str_))
print(palindrome_pointers(str_))
