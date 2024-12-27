# find the subarray whose product is maximum

# arr = [2,3,-2,4]
# ans = 6


def main(nums):
    # brute force
    # tc - O(n^2)
    # sc - O(1)
    maxprod = 0
    for i in range(len(nums)):
        prod = 1
        for j in range(i, len(nums)):
            prod *= nums[j]
            maxprod = max(prod, maxprod)

    return maxprod


def main1(nums):
    # we need to use prefix and suffix concept
    prefix = 1
    suffix = 1
    prod_result = 0
    for i in range(len(nums)):
        prefix *= nums[i]  # this will calculate the prod from start
        suffix *= nums[len(nums) - 1 - i]  # this will caluculate the prod from the end

        prod_result = max(prod_result, max(prefix, suffix))

        # if any element is 0 in the array then start the prefix/suffix again
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1

    return prod_result


print(main([2, 3, -2, 4]))
print(main1([2, 3, -2, 4]))
