# find the lower bound-> smallest index such that nums[index] >= target

def main(nums, target):
    # tc - O(logn) bianry search
    # sc - O(1)

    low = 0 
    high = len(nums) - 1
    ans = len(nums) # an assumption if we cant find any number in the array then 
    # the len(nums) is our lower bound which is one index greater than the last index
    while low <= high:

        mid = low + ((high - low) // 2)

        if nums[mid] >= target:
            ans = mid
            high = mid - 1 # go towards to see if we have further values samller than this mid
        else:
            low = mid + 1
    return ans

print(main([1,2,3,4,5], 1))

