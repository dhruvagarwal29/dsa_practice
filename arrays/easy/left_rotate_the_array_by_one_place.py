# left rotate the array by one place


def main(nums):
    # time complexity is O(n), space is O(1)

    temp = nums[0]

    for i in range(len(nums) - 1):
        nums[i] = nums[i + 1]
    nums[-1] = temp

    return nums


print(main([1, 2, 3, 4, 5]))
