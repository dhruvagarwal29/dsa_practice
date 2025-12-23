# we have an array which consists of duplicate element but one element is single,
# just give me that single element


def main(nums):
    # brute force
    # tc - O(n)

    for i in range(len(nums)):

        if i == 0:  # if the first element is single
            if nums[i] != nums[i + 1]:
                return nums[i]
        elif i == len(nums) - 1:  # if the second element is single
            if nums[i] != nums[i - 1]:
                return nums[i]
        else:  # if any middle element is single, here we put this is last as nums[i+1]
            # will fail at last element so 2nd if condition will check that
            if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
                return nums[i]


print(main([1, 2, 2, 3, 3]))
print(main([1, 1, 2, 3, 3]))
print(main([1, 1, 2, 2, 3]))

# we need to optimize the above code, sortede array, binary search


def main1(nums):
    # tc - O(logn)
    # here we will write some edge cases first
    if len(nums) == 1:
        return nums[0]

    # we are checking 1st element is single or not
    if nums[0] != nums[1]:
        return nums[0]
    # we are checking last element is single or not
    if nums[len(nums) - 1] != nums[len(nums) - 2]:
        return nums[len(nums) - 1]

    # now we can use binary search where our low will start from 1 and high - len(nums)-2

    # here we will use even and odd concept for index
    """
    [0,1,2,3,4,5,6,7,8,9,10] - indices for below array 
    [1,1,2,2,3,3,4,5,5,6,6]

    if we observe that before the single element ie 4 in the array the duplicate nos are 
    at (even, odd) position -- 1,1 are at 0,1 ; 2,2 are at 2,3
    and after 4 position changes to (odd, even) -- 5,5 are at 7,8
    6,6 are at 9,10 

    so one finding from here 

    (even, odd) position before single element
    (odd, even) posiiton after single element

    means these conditions can help us in eleminatinating the other half

    """

    low = 1
    high = len(nums) - 2

    while low <= high:
        mid = low + ((high - low) // 2)

        if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
            return nums[mid]
        elif (mid % 2 == 1 and nums[mid] == nums[mid - 1]) or (
            mid % 2 == 0 and nums[mid] == nums[mid + 1]
        ):
            low = mid + 1
            """
            (even, odd) position before single element
            (odd, even) posiiton  after single element
            
            we are standing at odd index and if previous elemet is 
            same as mid element then element the left half or if mid is 
            even then mid+1 element should be same as mid then eliminate 
            left half otherwise else eliminate right"""
        else:
            high = mid - 1

    return -1


print(main1([1, 2, 2, 3, 3]))
print(main1([1, 1, 2, 3, 3]))
print(main1([1, 1, 2, 2, 3]))
print(main1([1, 1, 2, 2, 3, 3]))
