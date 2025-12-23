# find the peak element, array can have multiple peaks
# arr[i-1] < arr[i] > arr[i+1]

""" 
1) ar = [1,2,3,4,5,6,7,8,5,1] # ans is 8

2)  ar = [1,2,1,3,5,6,4], there are 2 different peaks 2,6, we can return any peak

3)  ar = [1,2,3,4,5] # there is no peak as such but in ques it is given that -inf is in the
start and end of index so the max element in the array is ans
"""


def main(nums):

    for i in range(0, len(nums)):
        if i == 0:
            if nums[i] > nums[i + 1]:
                return nums[i]
        elif i == len(nums) - 1:
            if nums[i] > nums[i - 1]:
                return nums[i]
        else:
            if nums[i] > nums[i + 1] and nums[i] > nums[i - 1]:
                return nums[i]


# print(main([1, 2, 3, 4, 5, 6, 7, 8, 5, 1]))
# print(main([1, 2, 1, 3, 5, 6, 4]))
# print(main([1, 2, 3, 4, 5]))
# print(main([5, 4, 3, 2, 1]))


def main1(nums):
    # i can write the above condition as this too
    # tc - O(n)
    # sc - O(1)
    for i in range(0, len(nums)):
        if ((i == 0) or (nums[i - 1] < nums[i])) and (
            (i == len(nums) - 1) or (nums[i] > nums[i + 1])
        ):
            return nums[i]


# print(main1([1, 2, 3, 4, 5, 6, 7, 8, 5, 1]))
# print(main1([1, 2, 1, 3, 5, 6, 4]))
# print(main1([1, 2, 3, 4, 5]))
# print(main1([5, 4, 3, 2, 1]))

# we can optimize this using binary search, using BS as some of the portion of
# array which is sorted


def main2(nums):
    # tc - O(logn)
    # we will check for the edge cases first
    if len(nums) == 1:
        return nums[0]

    # If first element is greater than second element this is the peak
    if nums[0] > nums[1]:
        return nums[0]

    # If last element is greater than second last element this is the peak
    if nums[len(nums) - 1] > nums[len(nums) - 2]:
        return nums[len(nums) - 1]

    # now our low = 1, high = len(nums) - 2

    low = 1
    high = len(nums) - 2

    while low <= high:
        mid = low + ((high - low) // 2)

        if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
            return nums[mid]
        elif nums[mid] > nums[mid - 1]:  # this means that peak is on right
            low = mid + 1
        else:  # nums[mid] > nums[mid+1]
            high = mid - 1


print(main2([1, 2, 3, 4, 5, 6, 7, 8, 5, 1]))
print(main2([1, 2, 1, 3, 5, 6, 4]))
print(main2([1, 2, 3, 4, 5]))
print(main2([5, 4, 3, 2, 1]))
