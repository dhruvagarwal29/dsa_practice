def main(nums):
    # Time complexity is O(n)
    for i in range(len(nums) - 1):
        if nums[i] <= nums[i + 1]:
            continue
        else:
            return False
    return True


print(main([1, 2, 3, 4, 5]))
print(main([1, 2, 6, 4, 2]))
