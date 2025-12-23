"""
424. Longest Repeating Character Replacement
You are given a string s and an integer k. You can
choose any character of the string and change it to any
other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing
the same letter you can get after performing the above operations.
"""


def brute_force(s, k):

    max_len = 0
    for i in range(len(s)):
        hashmap = {}
        max_freq = 0
        for j in range(i, len(s)):
            hashmap[s[j]] = 1 + hashmap.get(s[j], 0)

            max_freq = max(max_freq, max(hashmap.values()))
            window_len = j - i + 1

            if window_len - max_freq <= k:
                max_len = max(max_len, window_len)
            else:
                break

    return max_len


print(brute_force(s="ABAB", k=2))
