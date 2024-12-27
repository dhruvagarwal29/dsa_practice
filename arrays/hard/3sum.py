# find all unique triplets whose sum == 0 ; i != j!= k


def main(nums):
    # brute force
    # tc - O(n^3) * log(no of unique triplets)
    # sc - O(2 * no of inputs)
    # arr = []  # this will store duplicates
    # use set to store and we have to sort the array before storing
    array_set = set()
    temp = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):

                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    temp = [nums[i], nums[j], nums[k]]
                    temp.sort()
                    array_set.add(tuple(temp))

    return array_set


# better - try to make O(n^2), will try to remove one loop from above


def main1(nums):
    # we will use hashmap to save one loop
    # tc - O(n^2)
    # sc - O(2n)
    array_set = set()
    temp = []
    for i in range(len(nums)):
        hashset = set()
        for j in range(i + 1, len(nums)):
            rem = -(nums[i] + nums[j])

            if rem in hashset:
                temp = [nums[i], nums[j], rem]
                temp.sort()
                array_set.add(tuple(temp))
            else:
                hashset.add(nums[j])

    return array_set


# optimal sol
# we will use two pointer approach, sort the array.


def main2(nums):
    # tc - O(nlogn) + O(n^2)
    # sc - O(n)

    nums.sort()  # sorting so it will be easier to bypass duplicates and use 2 pointers
    ans = []
    for i in range(len(nums)):

        if i > 0 and nums[i] == nums[i - 1]:
            continue
        else:
            left = i + 1
            right = len(nums) - 1

            while left < right:
                target = nums[i] + nums[left] + nums[right]
                if target < 0:
                    left += 1
                elif target > 0:
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

    return ans


print(main([-1, 0, 1, 2, -1, -4]))
print(main1([-1, 0, 1, 2, -1, -4]))
print(main2([-1, 0, 1, 2, -1, -4]))
