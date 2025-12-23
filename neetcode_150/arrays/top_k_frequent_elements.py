"""
Given an integer array nums and an integer k,
return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.
Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]
"""

import heapq


def main(nums, k):
    # most frequent elements means who has high frequency, create min heap
    # the last two elements in heap is the most frequent
    hashmap = {}
    for i in nums:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1
    minheap = []
    for key, val in hashmap.items():
        heapq.heappush(minheap, (val, key))
        if len(minheap) > k:
            heapq.heappop(minheap)

    res = []

    for i in range(k):
        res.append(heapq.heappop(minheap)[1])

    return res


print(main(nums=[1, 2, 2, 3, 3, 3], k=2))
