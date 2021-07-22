# Write a program that checks whether an integer is a palindrome. For example, 121 is a palindrome, as well as 888.
# 678 is not a palindrome. Do not convert the integer into a string.

# after lots of thoughts, i think i can use mod to get the reverse version of thg original num

def is_numeric_palindrome(n: int) -> bool:
    assert n > 0

    m = 0
    v = n
    while v > 10:
        r = v % 10
        v /= 10
    return n == m


assert is_numeric_palindrome(3)
assert is_numeric_palindrome(121)
assert not is_numeric_palindrome(678)
assert not is_numeric_palindrome(54)