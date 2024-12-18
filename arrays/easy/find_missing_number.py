# find the missing number in an array
def main(nums):
    # this is brute force solution and time complesxity is O(n^2)
    # space is O(1)
    for i in range(1, len(nums) + 1):
        if i not in nums:
            return i


def main1(nums):
    # THIS IS  better solution but not optimal as we can decrease space in it
    # time complexity  - O(n)
    # space complexity - O(n)
    arr = [0] * (len(nums) + 2)

    for i in nums:
        arr[i] = 1

    for i in range(1, len(nums) + 1):
        if arr[i] == 0:
            return i


def main2(nums):
    # use sum way
    # sum of n nos
    # time complexity - O(n), space - O(1)
    N = len(nums) + 1
    total_sum = (N * (N + 1)) // 2
    arry_sum = sum(nums)
    return total_sum - arry_sum


def main3(nums):
    # this is better solutoin for large array sizes
    # it will take O(n) time complexity
    xor1, xor2 = 0, 0
    for i in range(0, len(nums)):
        xor2 = xor2 ^ nums[i]
        xor1 = xor1 ^ (i + 1)
    xor1 = xor1 ^ nums[-1]
    return xor1 ^ xor2


print(main([1, 2, 4, 5]))
print(main1([1, 2, 4, 5]))
print(main2([1, 2, 4, 5]))
print(main3([1, 2, 4, 5]))
