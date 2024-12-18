def main(nums):
    # brute force use extra space of O(n), time complexity - O(n)

    arr = len(nums) * [0]
    i = 0
    for n in nums:
        if n != 0:
            arr[i] = n
            i += 1

    return arr


def main1(nums):
    # we use two pointers

    left = 0
    right = 0

    while right < len(nums):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1
    return nums


print(main1([1, 0, 2, 3, 2, 0, 0, 4, 5, 1]))
