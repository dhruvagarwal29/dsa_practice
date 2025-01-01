# find no of occurrences of duplicated in sorted array
# we can use the concept of binary search, we used in first_last occurrence of element 
# and count those first and last occurrence


def first_occurrence(nums, target):
    low = 0 
    high = len(nums) -1 
    first = -1

    while low <= high:
        mid = low + ((high- low)//2)

        if nums[mid] == target:
            first = mid
            high = mid - 1 
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return first

def last_occurence(nums, target):
    low = 0 
    high = len(nums) - 1
    last = -1

    while low <= high:
        mid = low + ((high - low) // 2)

        if nums[mid] == target:
            last = mid
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return last
    
def main(nums, target):
    start, last = first_occurrence(nums, target), last_occurence(nums, target)

    return last - start + 1

print(main([2,4,6,8,8,8,11,13], 8))