# find the floor and ceil in the sorted array
# floor -> largest number in array <= x
# ceil -> smallest number in array >= x

# ar = [ 10,20,30,40,50], x = 25
# floor = 20
# ceil = 30

def main_ceil(nums, target):
    low = 0
    high = len(nums) - 1
    ceil = -1

    while low <= high:
        mid = low + ((high - low)//2)

        if nums[mid] >= target:
            ceil = nums[mid]
            high = mid - 1
        else:
            low = mid + 1

    return ceil

def main_floor(nums, target):
    low = 0 
    high = len(nums) - 1
    floor = -1

    while low <= high:
        mid = low + ((high-low)//2)

        if nums[mid] <= target:
            floor = nums[mid]
            low = mid + 1 # this will check for right array for largest
        else:
            high = mid - 1
    
    return floor

print(main_ceil([10,20,30,40,50], 25))
print(main_floor([10,20,30,40,50], 25))

print(main_ceil([10,20,25,40,50], 25))
print(main_floor([10,20,25,40,50], 25))