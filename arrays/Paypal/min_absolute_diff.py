def min_diff(nums):
    nums.sort()
    result = []
    min_diffi = float("inf")

    for i in range(1, len(nums)):
        diff = abs(nums[i] - nums[i - 1])

        if diff < min_diffi:
            min_diffi = diff
            result = [[nums[i - 1], nums[i]]]
        elif diff == min_diffi:
            result.append(nums[i - 1,], nums[i])

    return result
