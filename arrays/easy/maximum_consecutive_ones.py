# find the maximum consecutive ones


def main(nums):
    maxi = 0
    count = 0

    for i in nums:
        if i == 1:
            count += 1
        else:
            count = 0
        maxi = max(count, maxi)

    return maxi


print(main([1, 1, 0, 1, 1, 1, 0, 1, 1]))
