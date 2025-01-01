# Upper bound smallest index such  that arr[index] > x

def main(nums, target):
    low = 0 
    high = len(nums) - 1
    ans = len(nums)
    while low <= high:
        mid = low +((high - low)//2)

        if nums[mid] > target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


print(main([2,3,6,8,8,11,11,12], 6))
print(main([2,3,6,7,8,8,11,11,11,12], 11))
print(main([2,3,6,7,8,8,11,11,11,12], 12))
print(main([2,3,6,7,8,8,11,11,11,12], 13))
print(main([2,3,6,7,8,8,11,11,11,12], 0))

