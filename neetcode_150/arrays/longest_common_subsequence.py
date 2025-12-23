"""
Given an array of integers nums, return the length of the
longest consecutive sequence of elements that can be formed.
A consecutive sequence is a sequence of elements in which
each element is exactly 1 greater than the previous element. The elements do not have to be
consecutive in the original array.
You must write an algorithm that runs in O(n) time.
Input: nums = [2,20,4,10,3,4,5]
Output: 4
"""


def main(nums):
    nums_set = set(nums)
    longest = 0

    for n in nums:
        # check the start of the sequence
        if (n - 1) not in nums_set:
            length = 0
            while n + length in nums_set:
                length += 1
            longest = max(longest, length)
    return longest


print(main([100, 4, 200, 1, 3, 2]))
