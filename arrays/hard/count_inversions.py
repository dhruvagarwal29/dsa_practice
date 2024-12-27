# given array of integers, task is to find out no of pairs, where left element > right element


def main(nums):
    # brute force
    # tc - O(n^2)
    # sc - O(1)
    cnt = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                cnt += 1

    return cnt


print(main([5, 3, 2, 4, 1]))


# before solving above ques we can solve this question, let's say we have 2 sorted array
# and we need to find the pairs from the arrays where left element of 1st array is greater
# than the second element of 2nd array


def modified_pairs(nums1, nums2):
    # here we are checking if left element means element from nums1 is greater than right
    # element then all the reamining element in nums1 will be greater than right element
    # so add the remaining length of the array from left to end as all can make pairs
    # with right element and increase the right
    # if that is not the case then increase left

    # this is a very good intuition for this type of question
    # tc - O( n1 + n2) n1 - len(nums1), n2 - len(nums2)
    # sc - O(1)

    # but this is only possible if these are sorted arrys
    left = 0
    right = 0
    cnt = 0
    while left < len(nums1):

        if nums1[left] > nums2[right]:
            cnt += len(nums1[left:])
            right += 1
        else:
            left += 1

    return cnt


print(modified_pairs([2, 3, 5, 6], [2, 2, 4, 4, 8]))


# we will use the above approach to solve the count_inversions problem using merge sort algo
# we will split the arrays as we do in merge sort


# we will write the merge sort


def merge(left, right):
    i, j, cnt = 0, 0, 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            cnt += j - i + 1
            j += 1

    result += left[i:]
    result += right[j:]

    return result, cnt


def mergesort(nums):
    cnt = 0
    if len(nums) < 2:
        return nums, 0

    mid = len(nums) // 2

    left, x = mergesort(nums[:mid])
    cnt += x
    right, y = mergesort(nums[mid:])
    cnt += y

    arr, z = merge(left, right)

    cnt += z

    return arr, cnt


def main2(nums):

    return mergesort(nums)


print(main2([5, 3, 2, 4, 1]))

# this is a really good question
# tc- O(nlogn)
# sc - O(1) otherwise I am distorting the original arry
