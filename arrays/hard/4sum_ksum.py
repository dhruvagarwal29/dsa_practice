# given an array, find 4 different indexes such that whose numbers gives a target


def main(nums, target):
    hashset = set()
    # tc - O(n^4)
    # sc - O(2n)

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                for l in range(k + 1, len(nums)):
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    if total == target:
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        temp.sort()
                        hashset.add(tuple(temp))

    return hashset


# better sol - we can use hashmap to remove one loop to make it O(n^3)


def main1(nums, target):
    # tc - O(n^3)
    # sc - O(2n) + O(unique triplets)
    array_set = set()
    temp = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            hashset = set()
            for k in range(j + 1, len(nums)):
                rem = target - (nums[i] + nums[j] + nums[k])
                if rem in hashset:
                    temp = [nums[i], nums[j], nums[k], rem]
                    temp.sort()
                    array_set.add(tuple(temp))
                else:
                    hashset.add(nums[k])

    return array_set


# this is not good as we are using hashset to store and lookup, need to get rid of that
# tc is ok in above but not space

# optimal, will use two pointer


def main2(nums, target):
    # sort num
    # tc - O(n^3)
    # sc - O(n)
    nums.sort()
    ans = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        else:
            for j in range(i + 1, len(nums)):
                if j > 1 and nums[j] == nums[j - 1]:
                    continue
                else:
                    left = j + 1
                    right = len(nums) - 1
                    while left < right:
                        total = nums[i] + nums[j] + nums[left] + nums[right]
                        if total < 0:
                            left += 1
                        elif total > 0:
                            right -= 1
                        else:
                            ans.append([nums[i], nums[j], nums[left], nums[right]])
                            left += 1
                            right -= 1

                            while left < right and nums[left] == nums[left - 1]:
                                left += 1

                            while left < right and nums[right] == nums[right + 1]:
                                right -= 1

    return ans


print(main([1, 0, -1, 0, -2, 2], 0))
print(main1([1, 0, -1, 0, -2, 2], 0))
print(main2([1, 0, -1, 0, -2, 2], 0))
