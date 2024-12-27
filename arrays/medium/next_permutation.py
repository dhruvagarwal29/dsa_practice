# given the array of integers you have to give the next largest permutation

# brute force is recursion, need to check that
# tc - O(n*n!)
# as no of permutions of any number is n!


# optimal solution

# intuition->
# [2,1,5,4,3,0,0]

# 1) try to get the as longer prefix match possible, if we see in above example,
# if we go backwards, to find the longer prefix we can see that from 0->5 everything
# is increasing and 1 is decreasing after 5 so means we need to swap 1 by the next
# largest number

# 2) find the number which is just next after 1 in the array that is 3 and swap

# 3) now after placing 2,3, we need to put the remaining array in ascending order so it
# makes 2,3 the greatest prefix, to do so we can just reverse the remaining array


def main(nums):

    # so to find the larger prefix, we need to see what is the last element which
    # can make the aray next big array i e 2 last index of the array
    # eg - 1,2,3,4,5 -> 1,2,3,5,4 -- here we can see that the possibility of
    # next big array lies in the 2nd last index so just start from here and go till
    # zero to find the dip (number where we have to swap)
    index = -1

    for i in range(len(nums) - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            index = i
            break

    if index == -1:  # means there is no big number present in the array (5,4,3,2,1)
        return nums[::-1]

    for i in range(len(nums) - 1, index, -1):
        if nums[i] > nums[index]:
            nums[i], nums[index] = nums[index], nums[i]
            break

    nums[index + 1 :] = reversed(nums[index + 1 :])

    return nums


print(main([1, 2, 3]))
print(main([3, 2, 1]))
