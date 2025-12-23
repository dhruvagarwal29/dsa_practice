"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring
without duplicate characters
"""


def brute_force(s):
    max_len = 0
    for i in range(len(s)):
        char_set = set()
        for j in range(i, len(s)):
            if s[j] in char_set:
                break
            else:
                char_set.add(s[j])

            max_len = max(max_len, len(char_set))

    return max_len


print(brute_force("cadbzatf"))


def optimal(s):
    left = 0
    max_len = 0
    hash_map = {}

    for right in range(len(s)):

        if s[right] in hash_map:
            # update the left pointer with the present number
            left = max(left, hash_map[s[right]])

        max_len = max(max_len, len(hash_map))
        hash_map[s[right]] = right + 1  # as we have this in the left so + 1

    return max_len


print(optimal("cadbzatf"))

### easy way to do it using set and remove functionality


def optimal_easy(s):
    left = 0
    max_len = 0
    char_set = set()

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_len = max(max_len, len(char_set))

    return max_len


print(optimal_easy("cadbzatf"))
