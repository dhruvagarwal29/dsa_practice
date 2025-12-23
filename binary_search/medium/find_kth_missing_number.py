"""
given an increasing +ve nos array, find the kth missing number
"""

# ans = [2,3,4,7,11], k = 5


def main(nums, k):
    # this is a good brute force technique
    # tc - O(n)
    """
    let say 1 st num in array is 2 and we have k = 1
    then the missing 1st number is 1 as k is smaller than 2
    but if let's say k = 2
    then we can see that 2 is present, 3 is present, 4 is present, means
    they will take their place in the array, so we will just increase the k value
    k will be 2 then 3, then 4, then 5, next element comes as 7, where k which is 5 is smaller
    then 7, so this is the second element which is missing from the element

    """

    for n in nums:
        if n <= k:
            k += 1
        else:
            break

    return k


# print(main([2, 3, 5, 6, 7], k=1))
# print(main([2, 3, 4, 6, 7], k=2))
# print(main([2, 3, 4, 7], k=3))
# print(main([1, 2, 3, 4], k=2))


def main1(nums, k):
    # we will use Binary search in it, but it is not a conventional solu
    # we need to first find the indexes from the array where we can say,
    # my missing number will be in between these indices

    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        missing_num = nums[mid] - (mid + 1)
        ## mid + 1 is the index which represent the original numnber should be at place

        if missing_num < k:
            low = mid + 1
        else:
            high = mid - 1

    return low + k


print(main1([2, 3, 5, 6, 7], k=1))
print(main1([2, 3, 4, 6, 7], k=2))
print(main1([2, 3, 4, 7], k=3))
print(main1([1, 2, 3, 4], k=2))
print(main1([2, 3], 1))
