# give the maximum sum of subarray


def main(nums):
    # brute force
    # tc - O(n^2), sc - O(1)
    max_sum = float("-inf")
    for i in range(len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]
            max_sum = max(max_sum, sum)

    return max_sum


# optimal solution using kadane's algo


def main1(nums):
    sum = 0
    max_sum = 0

    for i in nums:
        sum += i
        max_sum = max(sum, max_sum)

        if sum < 0:
            sum = 0

    return max_sum


# now the follow up in this is we need to print the array too
# we can see that whenever we are have our sum getting increased it is doing so
# after sum=0, we can have two pointer


def main2(nums):
    # give me the array

    sum = 0
    max_sum = 0

    for i in range(len(nums)):

        if sum == 0:
            # making our start index as i whenever we have sum as 0
            start_index = i

        sum += nums[i]

        if sum > max_sum:
            max_sum = sum
            ans_start = start_index
            ans_end = i

        if sum < 0:
            sum = 0

    return max_sum, (ans_start, ans_end)


print(main([-2, -3, 4, -1, -2, 1, 5, -3]))
print(main1([-2, -3, 4, -1, -2, 1, 5, -3]))
print(main2([-2, -3, 4, -1, -2, 1, 5, -3]))
