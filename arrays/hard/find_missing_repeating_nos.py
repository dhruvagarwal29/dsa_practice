# find the missing and repeating elements from the array


def main(nums):
    # brute force
    # tc - O(n^2)
    # sc - O(1)
    n = max(nums)
    repeating, missing = -1, -1

    for i in range(1, n):
        cnt = 0

        for j in range(0, n - 1):
            if nums[j] == nums[i]:
                cnt += 1

        if cnt == 2:
            repeating = i
        elif cnt == 0:
            missing = i

        if missing != -1 and repeating != -1:
            break

    return missing, repeating


# better sol - we will use hashmap or hasharray


def main1(nums):
    # tc - O(n) + O(n)
    # sc - O(n) for hasharray
    n = max(nums)
    repeating = -1
    missing = -1
    hasharr = [0] * (n + 1)

    for i in nums:
        hasharr[i] += 1

    for i in range(1, n):
        if hasharr[i] == 2:
            repeating = i
        elif hasharr[i] == 0:
            missing = i

        if missing != -1 and repeating != -1:
            break

    return missing, repeating


# we need to remove the extra space

# we will use maths formulas here, making 2 equations


def main2(nums):
    # optimal sol
    # tc - O(n)
    # sc - O(1)
    # x - repeating, y - missing
    x, y = -1, -1
    n = max(nums)

    # need to make 2 equations one will be from addintion of normal nos
    # other will be from add of squares of these nos
    sn, s2n = 0, 0  # these are sums of nums and squares of nums element

    for i in nums:
        sn += i
        s2n += i**2

    # through maths we know that total sum of n numbers
    ts = (n * (n + 1)) // 2
    t2s = (n * (n + 1) * ((2 * n) + 1)) // 6

    # so now we have  2 equations
    # sn - ts = x-y              # ----(1)
    # s2n - t2s = x**2 - y**2      # ----(2)

    # we can write x**2 - y**2 == (x+y) (x-y) and we know x-y from eq 1

    # s2n - t2s = (x+y) * (sn - ts)
    # (s2n - t2s) / (sn - ts) = (x+y) ---(3)
    # we got (x+y) and (x-y)
    val1 = sn - ts  # x-y
    val2 = s2n - t2s
    val2 = val2 / val1  # x+y
    x = (val1 + val2) // 2
    y = x - val1

    return int(x), int(y)


## xor solution
def main3(nums):
    # tc - O(4n) ~ O(n)
    # sc - O(1)
    # x - repeating, y - missing
    n = len(nums)
    xor = 0
    for i in range(0, n):
        xor ^= nums[i]
        xor = xor ^ (i + 1)

    # find the bit number
    bit_no = 0
    while True:
        if (xor & (1 << bit_no)) != 0:
            break
        bit_no += 1

    # we got the bit number, now we will make 2 groups, zero grp and one group
    zero_grp = 0
    one_grp = 0

    for i in range(0, n):  # for the array
        if (nums[i] & (1 << bit_no)) != 0:  # part of 1th club
            one_grp ^= nums[i]
        else:
            zero_grp ^= nums[i]  # part of 0th club

    # now need to same thing for array
    for i in range(1, n + 1):
        if (i & (1 << bit_no)) != 0:  # part of 1th club
            one_grp ^= i
        else:
            zero_grp ^= i

    cnt = 0
    for i in range(0, n):
        if nums[i] == zero_grp:
            cnt += 1

    if cnt == 2:
        return (zero_grp, one_grp)
    else:
        return (one_grp, zero_grp)


print(main([1, 1, 2, 3, 4, 6]))
print(main1([1, 1, 2, 3, 4, 6]))
print(main2([1, 1, 2, 3, 4, 6]))
print(main3([1, 1, 2, 3, 4, 6]))
