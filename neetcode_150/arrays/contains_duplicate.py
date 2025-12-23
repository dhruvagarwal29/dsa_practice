"""
Given an integer array nums, return true if any
value appears more than once in the array, otherwise return false.
nums = [1, 2, 3, 3]
"""


def main(nums):

    # hashmap, dict, count 1 : 1, 2 :1, 3: 2
    hashmap = {}

    for i in nums:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1

    for k, v in hashmap.items():
        if v > 1:
            return True

    return False


print(main([1, 2, 3, 3]))

print(main([1, 2, 3]))
