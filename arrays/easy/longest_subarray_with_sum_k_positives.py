# give me the longest subarray whose sum = k


def main(nums, k):
    arr = []
    max_len = 0
    for i in range(0, len(nums)):
        for j in range(i, len(nums)):
            s = 0
            for t in range(i, j):
                s += nums[t]
            if s == k:
                max_len = max(max_len, (j - i))
                arr.append(nums[i:j])

    return arr, max_len


def main1(nums, k):
    # this is brute force only just summing one loop outside, O(n^2)
    max_len = 0
    arr = []
    for i in range(len(nums)):
        s = 0
        for j in range(i, len(nums)):
            s += nums[j]

            if s == k:
                max_len = max(max_len, j - i + 1)
                arr.append(nums[i : j + 1])

    return max_len, arr


def main2(nums, k):
    # this approach only works for positive numbers not  for nums containing 0's or -ve's
    # this is a better approach then above, time complexity is O(n), space - O(n)
    # in this approach we are saving sum from start in hashmap and check if prefix sum is
    # equal to k or not,

    hashmap = {}
    total = 0
    max_len = 0
    for i in range(len(nums)):
        total += nums[i]

        if total == k:
            max_len = max(max_len, i + 1)

        rem = total - k

        if rem in hashmap:
            leng = i - hashmap[rem]
            max_len = max(max_len, leng)

        if total not in hashmap:
            hashmap[total] = i

    return max_len


# OPTIMAL SOLUTION - 2 POINTERS APPROACH


def main3(nums, k):
    # we have 2 pointers start from 0, we keep increaing one of it,
    # if any point we get sum as k, we save the lenght and if keep increasing
    # if it exceeds k then we start increasing our second pointer
    # tc - O(2n), sc - O(1)
    left, right = 0, 0
    total = 0
    max_len = 0
    while right < len(nums):

        total += nums[right]
        if total == k:
            max_len = max(max_len, right - left + 1)

        while total > k:
            total -= nums[left]
            left += 1

        right += 1

    return max_len


print(main([1, 2, 4, 1, 1, 1, 3, 1], 3))
print(main1([1, 2, 4, 1, 1, 1, 3, 1], 3))
print(main2([1, 2, 4, 1, 1, 1, 3, 1], 3))
print(main3([1, 2, 4, 1, 1, 1, 3, 1], 3))
print(main3([1, 3, 5, 6, 7, 8, 9, 2], 2))
