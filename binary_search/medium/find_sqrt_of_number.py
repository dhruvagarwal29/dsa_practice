# find the sqrt of an integer


def main(n):
    # we can use math.sqrt fucntion

    x = n**0.5
    return int(x)


print(main(36))
print(main(23))


def main1(n):
    # using loop iterative method
    ans = 1
    for i in range(1, n):
        if i * i <= n:
            ans = i
        else:
            break

    return ans


print(main1(36))
print(main1(23))


# using binary search


def main2(n):
    low = 1
    high = n
    ans = 1
    while low <= high:
        mid = low + ((high - low) // 2)

        if mid * mid <= n:
            ans = mid
            low = mid + 1
        else:  # means the numbers from the mid towards right we need to decrease high
            high = mid - 1

    return ans


def main3(n):
    low = 1
    high = n

    while low <= high:
        mid = (low + high) // 2

        if mid * mid <= n:
            low = mid + 1
        else:
            high = mid - 1

    return high


"""
 we can also return high as high will start from the numbers which
 can not be the answers so it will decrease to the optimal sol eventually
"""


print(main2(36))
print(main2(23))
print(main3(23))
