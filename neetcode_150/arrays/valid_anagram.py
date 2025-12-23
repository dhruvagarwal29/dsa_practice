"""
Given two strings s and t, return true if the two strings are
anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as
another string, but the order of the characters can be different.
"""


def main(s, t):
    # two hashmap solution
    hash_s, hash_t = {}, {}

    if len(s) != len(t):
        return False

    for i in range(len(s)):
        hash_s[s[i]] = 1 + hash_s.get(s[i], 0)
        hash_t[t[i]] = 1 + hash_t.get(t[i], 0)

    return hash_s == hash_t


print(main("race", "pace"))
