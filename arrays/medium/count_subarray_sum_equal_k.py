# count the subarrays whose sum is equal to k


def main(nums, k):

    # brute force
    # o(n^2)
    # space is O(n), but printing all subarrays and maxlen is my addition
    cnt = 0
    arr = []
    max_len = 0

    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]

            if total == k:
                cnt += 1
                max_len = max(max_len, j - i + 1)
                arr.append(nums[i : j + 1])

    return cnt, arr, max_len


# optimal solution will use prefix sum concept as it has negatives too in this


def main1(nums, k):
    hashset = {0: 1}
    prefix_sum = 0
    cnt = 0
    for i in range(len(nums)):

        prefix_sum += nums[i]

        rem = prefix_sum - k
        if rem in hashset:
            cnt += hashset[rem]
        if prefix_sum in hashset:
            hashset[prefix_sum] += 1
        else:
            hashset[prefix_sum] = 1

    return cnt


print(main([1, 2, 3, -3, 1, 1, 1, 4, 2, -3], 3))
print(main1([1, 2, 3, -3, 1, 1, 1, 4, 2, -3], 3))
