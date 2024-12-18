# find 2 nos whose sum is equal target


def main(nums, target):
    # brute force
    # tc - O(n^2), sc - O(1)
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                return f"Possible, {i,j}"

    return "Not possible"


def main1(nums, target):
    # a better solution then above, using hashmap
    # tc -- O(n), sc - O(n)
    # this is 2 pass solu
    hashmap = {}

    for i in range(len(nums)):
        if nums[i] not in hashmap:
            hashmap[nums[i]] = i

    for i in range(len(nums)):
        rem = target - nums[i]

        if rem in hashmap:
            return f"Possible, {i , hashmap[rem]}"

    return "NotPossible"


def main2(nums, target):
    # this is same as above just with one pass
    # tc -- O(n), sc - O(n)
    hashmap = {}

    for i in range(len(nums)):
        rem = target - nums[i]

        if rem in hashmap:
            return f"Possible, {hashmap[rem], i}"

        hashmap[nums[i]] = i

    return "not Possible"


# optimal sol, without using hashmap, we will use two pointers,
# but for this we need array to be sorted
def main3(nums, target):
    # tc - O(nlogn), space O(1)
    nums.sort()
    left = 0
    right = len(nums) - 1

    while left != right:
        total = nums[left] + nums[right]

        if total == target:
            return f"Possible, {left, right}"
        elif total > target:
            right -= 1
        else:
            left += 1

    return "Not Possible"


print(main([1, 2, 3, 4, 5], 6))
print(main1([1, 2, 3, 4, 5], 6))
print(main2([1, 2, 3, 4, 5], 6))
print(main3([1, 2, 3, 4, 5], 6))
