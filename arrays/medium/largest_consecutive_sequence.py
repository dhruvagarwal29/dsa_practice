# given the array find the longest consecutive sequence

# brute force


def main(nums):
    # tc - O(n^2)
    for i in nums:
        maxi = 1
        cnt = 1
        while i + 1 in nums:
            i = i + 1
            cnt += 1
        maxi = max(cnt, maxi)

    return maxi


# better
def main1(nums):
    nums.sort()
    cnt = 0
    maxi = 0
    last_smallest = float("-inf")

    for i in nums:
        if i - 1 == last_smallest:
            cnt += 1
            last_smallest = i
        elif i != last_smallest:
            cnt = 1
            last_smallest = i

        maxi = max(maxi, cnt)

    return maxi


def main2(nums):
    nums_set = set(nums)

    maxi = 0
    for i in nums_set:
        cnt = 1
        if i - 1 not in nums:
            while i + 1 in nums:
                i += 1
                cnt += 1

            maxi = max(maxi, cnt)

    return maxi


print(main([102, 4, 100, 1, 101, 3, 2, 1, 1]))
print(main1([102, 4, 100, 1, 101, 3, 2, 1, 1]))
print(main2([102, 4, 100, 1, 101, 3, 2, 1, 1]))
