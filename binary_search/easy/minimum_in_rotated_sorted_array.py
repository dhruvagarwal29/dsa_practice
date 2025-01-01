# find the minimum in rotated sorted array


def main(nums):
    low = 0
    high = len(nums) - 1
    ans = float("inf")
    while low <= high:
        mid = low + ((high - low) // 2)

        if (
            nums[low] <= nums[mid]
        ):  # if this half is sorted then the low will stand at the lowest element maybe
            ans = min(ans, nums[low])
            low = mid + 1
        else:  # if this half is not sorted just make the mid as min if it is and decrease the high
            ans = min(ans, nums[mid])
            high = mid - 1

    return ans


print(main([4, 5, 1, 2, 3]))

# we can make it more optimal
# if nums[low] <= nums[high] then low is ur min
# we can break from here
