# u need to find an element in a rotated sorted array


def main(nums, target):
    # we cant eliminate one half here like in normal BS, we have to check in both
    # the halves but logically, we have to identify the sorted half and see
    # where our target lies and eliminate the other half
    # tc - O(logn) log base 2
    # sc - O(1)

    low = 0
    high = len(nums) - 1

    while low <= high:

        mid = low + ((high - low) // 2)

        if nums[mid] == target:
            return mid
        # now identify the sorted half
        elif nums[low] <= nums[mid]:

            if nums[low] <= target and target <= nums[mid]:
                high = mid - 1  # eliminate the right half
            else:
                low = mid + 1  # eliminate the left half
        else:  # the other is sorted, this is guranteed that one of the half will be sorted
            if nums[mid] <= nums[high] and target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


print(main([7, 8, 9, 1, 2, 3, 4, 5], 1))
