# find the first and last occurrence of x

 # brute force
def main(nums, x):
    # tc - O(n)
    first = -1
    last = -1 

    for i in range(len(nums)):
        if nums[i] == x:
            if first == -1:
                first = i 
            last = i 
    
    return first, last

# we willl use binary search in this, it will use lower bound and upper bound

def main1(nums, target):
    # here we can use lower bound and upper bound concept as they also in a way
    # gives the same thing, just in upper bound we have to - 1 
    # lower bound is smallest >= x which means it will give the starting point (first)
    # index of the element
    # upper bound is smallest element > x means a value which is just bigger than the x
    # ie why we are subtracting one from it

    # tc - O(2logn)
    # sc - O(1)

    # lower bound
    def lower_bound(nums, target):
        low = 0 
        high = len(nums) - 1
        lb = -1

        while low <= high:
            mid = low + ((high - low) // 2)

            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1

        return lb
    
    def upper_bound(nums, target):
        low = 0
        high = len(nums) - 1 
        hb = -1

        while low <= high:
            mid = low + ((high - low) // 2)

            if nums[mid] > target:
                hb = mid
                high = mid - 1
            else:
                low = mid + 1 
        
        return hb
    
    first = lower_bound(nums, target)
    if nums[first] != target or first == len(nums):
        # we dont need to check for upper bound here as if lower is not correct then upper
        # will not be correct as well
        return (-1,-1)
    
    last = upper_bound(nums, target)

    return first, last - 1

# interviewers may not be happy from this solution of lb and ub, so we can use BS directly

def main2(nums, target):
    low = 0
    high = len(nums) -1 
    first = -1
    last = -1

    # FINDING FIRST
    while low <= high:
        mid = low + ((high - low) // 2)

        if nums[mid] == target:
            first = mid
            high = mid - 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    
    # FINDING LAST
    low = 0
    high = len(nums) -1 
    while low <= high:
        mid = low + ((high - low) // 2)

        if nums[mid] == target:
            last = mid
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return first, last



print(main([2,4,6,8,8,8,11,13], 8))
print(main1([2,4,6,8,8,8,11,13], 8))      
print(main2([2,4,6,8,8,8,11,13], 8))     