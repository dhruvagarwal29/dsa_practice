# left rotate the array by d places
def main(nums, d):
    d = d % len(nums)
    # brute force, time complexity - O(n) + O(n) = O(2n), space - O(d)

    temp = nums[:d]

    for i in range(d, len(nums)):

        nums[i - d] = nums[i]
    j = 0
    for i in range(len(nums) - d, len(nums)):
        nums[i] = temp[j]
        j += 1

    return nums


def main1(nums, d):
    d = d % len(nums)
    # brute force, time complexity - O(n) + O(n) = O(2n), space - O(d)
    temp = nums[:d]
    for i in range(d, len(nums)):
        nums[i - d] = nums[i]

    for i in range(len(nums) - d, len(nums)):
        nums[i] = temp[i - (len(nums) - d)]

    return nums


# the optimal solution is quite simple, just the trick is u have to reverse the array
# first by 0->d, d -> len(arr) and last reverse the array


def main3(nums, d):

    d = d % len(nums)

    # first reverse the array from 0 to d
    reverse(nums, 0, d - 1)
    reverse(nums, d, len(nums) - 1)
    reverse(nums, 0, len(nums) - 1)

    return nums


def reverse(nums, fi, li):

    while fi <= li:
        nums[fi], nums[li] = nums[li], nums[fi]
        fi += 1
        li -= 1


print(main([1, 2, 3, 4, 5, 6, 7], 2))
print(main1([1, 2, 3, 4, 5, 6, 7], 2))
print(main3([1, 2, 3, 4, 5, 6, 7], 2))
print(main3([1, 2, 3, 4, 5, 6, 7], 3))
