# find the element in the array which appears more than N/2 times


def main(nums):

    # brute force
    # tc - O(n^2)
    # sc - O(1)

    for i in range(len(nums)):

        cnt = 0

        for j in range(len(nums)):

            if nums[i] == nums[j]:
                cnt += 1

        if cnt > len(nums) // 2:
            return f"{nums[i]} is the number and occurs {cnt} times"

    return f"No such number {-1}"


# better solution


def main1(nums):
    # this is a better solution
    # tc - O(2n)
    # sc - O(n)

    hashmap = {}

    for i in nums:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1

    for k, v in hashmap.items():
        if v > len(nums) // 2:
            return f"{k} is the number and occurs {v} times"

    return f"No such number {-1}"


# optimal algo is we need to minimize space - (Moore's voting algorithm)
# this algo is easy we just need to check if some number appears more than n/2 times
# it will not get cancelled as it has appears more than n/2 times


def main2(nums):
    # tc - O(2n)
    # sc - O(1)
    cnt = 0
    el = 0
    for i in range(len(nums)):

        if cnt == 0:
            cnt = 1
            el = nums[i]
        elif nums[i] == el:
            cnt += 1
        else:
            cnt -= 1

    # check if element we had  whose count is not zero is appearing more than n/2 times
    cnt1 = 0
    for i in range(len(nums)):
        if nums[i] == el:
            cnt1 += 1

    if cnt1 > len(nums) // 2:
        return f"{el} is the number and occurs {cnt1} times"

    return f"No such number {-1}"


print(main([2, 2, 1, 1, 3, 2, 2]))
print(main1([2, 2, 1, 1, 3, 2, 2]))
print(main2([2, 2, 1, 1, 3, 2, 2]))
