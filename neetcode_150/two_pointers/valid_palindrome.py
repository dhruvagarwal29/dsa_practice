"""
A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters
include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""


def main(s):
    left = 0
    right = len(s) - 1

    while left <= right:
        if not s[left].isalnum():
            left += 1
            continue
        elif not s[right].isalnum():
            right -= 1
            continue
        elif s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
