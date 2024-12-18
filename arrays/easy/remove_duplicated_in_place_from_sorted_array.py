def main(nums):
    # brute force use set, put in set but it will not be a in-place solution
    # to prepare the set it will take O(n) time and space complexity
    s = set(nums)

    return s


def main1(nums):
    # two pointers approach O(n)
    left = 0
    for right in range(1, len(nums)):
        if nums[left] != nums[right]:
            nums[left + 1] = nums[right]
            left += 1

    return nums


def main2(nums):
    left = 0
    right = 1

    while right < len(nums):
        if nums[left] != nums[right]:
            nums[left + 1] = nums[right]
            left += 1
        right += 1
    return nums


print(main2([1, 1, 2, 2, 2, 3, 3]))
