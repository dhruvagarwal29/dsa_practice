# find the index if value is present in the array, if not then give me the index 
# where it should be inserted while maitaining order

# it is like finding the lower bound

def main(nums, target):

    low = 0
    high = len(nums) - 1
    ans = len(nums)

    while low <= high:

        mid = low + ((high - low) // 2)

        if nums[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return ans

print(main([1,2,4,7], 6))
print(main([1,2,4,7], 2))
print(main([1,2,4,7], 3))