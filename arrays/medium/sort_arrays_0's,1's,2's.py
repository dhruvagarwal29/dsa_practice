# sort the arrays 0,1,2


def main(nums):
    # tc - nlogn, space - O(1)
    # sorting

    nums.sort()
    return nums


def main1(nums):
    # second approach count all 0,1,2
    # then loop on their count and chage the original array
    # tc - O(2n), space - O(1)
    a, b, c = 0, 0, 0
    for i in nums:
        if i == 0:
            a += 1
        elif i == 1:
            b += 1
        else:
            c += 1

    for i in range(a):
        nums[i] = 0

    for i in range(a, a + b):
        nums[i] = 1

    for i in range(a + b, a + b + c):
        nums[i] = 2
    return nums


# dutch national flag algorithm
def main2(nums):
    # will take 3 pointers
    # tc - O(n)
    # sc - O(1)
    low, mid = 0, 0
    high = len(nums) - 1

    while mid != high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            mid += 1
            low += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums


print(main([1, 0, 2, 1, 1, 0, 0, 2, 0]))
print(main1([1, 0, 2, 1, 1, 0, 0, 2, 0]))
print(main2([1, 0, 2, 1, 1, 0, 0, 2, 0]))
