# find the second largest element in the array


def main(nums):
    # first using sort
    # brute force nlong(n) + n
    nums.sort()
    # largest = nums[-1]
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] != nums[i + 1]:
            return nums[i]


def main1(nums):
    # find the largest in 1st pass and then find the 2nd largest in 2nd pass
    # time complexity O(n) +O (n) = O(2n), space is O(1)
    largest = 0
    for n in nums:
        if n >= largest:
            largest = n

    second_largest = 0

    for n in nums:
        if n < largest and n >= second_largest:
            second_largest = n

    return second_largest


def main2(nums):
    # time complexity - O(n)
    largest, second_largest = 0, 0
    for n in nums:
        if n > largest:
            second_largest = largest
            largest = n
        elif n < largest and n > second_largest:
            second_largest = n

    return second_largest


print(main([4, 2, 1, 7, 7, 5]))
print(main([4, 2, 1, 7, 7, 7, 7, 7]))

print(main1([4, 2, 1, 7, 7, 5]))
print(main1([4, 2, 1, 7, 7, 7, 7, 7]))

print(main2([4, 2, 1, 7, 7, 5]))
print(main2([4, 2, 1, 7, 7, 7, 7, 7]))
