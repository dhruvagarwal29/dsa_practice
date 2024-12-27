# merge sort
# divide the array untill u reaches the last 2 elements and merge them based
# on their weight


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result


def mergesort(nums):
    if len(nums) < 2:
        return nums

    mid = len(nums) // 2

    left = mergesort(nums[:mid])
    right = mergesort(nums[mid:])

    return merge(left, right)


print(mergesort([2, 4, 1, 5, 7]))
