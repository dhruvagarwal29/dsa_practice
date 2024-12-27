# count of subarrays whose count is k

# brute force


def main(nums, k):
    # tc - O(n^3)
    # sc - O(1)
    cnt = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            xor = 0
            for k in range(i, j + 1):
                xor = xor ^ nums[k]
                if xor == k:
                    cnt += 1

    return cnt


# better we can remove kth loop
def main1(nums, k):
    cnt = 0
    for i in range(len(nums)):
        xor = 0
        for j in range(i, len(nums)):
            xor = xor ^ nums[j]
            if xor == k:
                cnt += 1

    return cnt


# we will use prefix sum concept as prefix xor
# optimal sol, we will have hashmap which will take the count of xor on the fly


def main2(nums, k):
    # tc - O(n)
    # sc - O(n)
    hashmap = {0: 1}
    cnt = 0
    xor = 0
    for i in nums:
        xor ^= i
        prefix_xor = xor ^ k
        if prefix_xor in hashmap:
            cnt += hashmap[prefix_xor]
        if xor in hashmap:
            hashmap[xor] += 1
        else:
            hashmap[xor] = 1

    return cnt, hashmap


print(main([4, 2, 2, 6, 4], 6))
print(main1([4, 2, 2, 6, 4], 6))
print(main2([4, 2, 2, 6, 4], 6))
