# find the number that appears once in array
def main(nums):
    arr = []
    # this is brute force, will take O(n^2) time complexity , O(n) space
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                count += 1

        if count == 1:
            arr.append(nums[i])

    return arr


def main1(nums):
    # this is better than above O(n) time comp, O(n) space
    arr = [0] * (max(nums) + 1)

    for i in nums:
        arr[i] += 1

    for i in range(len(arr)):
        if arr[i] == 1:
            return i


def main2(nums):
    hashmap = {}
    for i in nums:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1

    for k, v in hashmap.items():
        if v == 1:
            return k


def main3(nums):
    xor = 0

    for i in nums:
        xor = xor ^ i

    return xor


print(main([1, 1, 2, 3, 3, 4, 5]))
print(main1([1, 1, 2, 2, 3]))
print(main1([1, 2, 2, 3, 3]))
print(main2([1, 2, 2, 3, 3]))
print(main3([1, 2, 2, 3, 3]))
