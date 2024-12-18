# array is given with n nos, n/2 is -ve and n/2 is +ve, so we have to arrange them
# in alternate sign nos


def main(nums):
    # brute force, make two new arrays, +ve, -ve and pass them accordingly
    # time complexity = O(n) + O(n)
    # space complexity = O(n)
    posi = []
    negi = []

    for i in nums:
        if i < 0:
            negi.append(i)
        else:
            posi.append(i)

    # we know that positive nos will be at even positions
    # and -ve nos will be at odd positions

    for i in range(len(nums) // 2):

        nums[2 * i] = posi[i]
        nums[2 * i + 1] = negi[i]

    return nums


# in this we can do it in one pass, but we cannot remove space


def main1(nums):
    # two pointers approach, put positve nos at posi pointer and -ve nos at negi pointer
    # tc - O(n), sc - O(n)
    posi = 0
    negi = 1
    arr = [0] * len(nums)

    for i in nums:
        if i > 0:
            arr[posi] = i
            posi += 2
        else:
            arr[negi] = i
            negi += 2

    return arr


# now we have a new variety of question where it states that if the no of +ve and -ve
# nos is not same as in above question, means +ve , -ve can be in any order
# so till the length is same we need to put in alternate way, after that just add the
# remaining ones
# for this we need to fall back to brute force sol


def main2(nums):
    # tc - O(N) + O(N)
    # sc - O(N)
    posi = []
    negi = []

    for i in nums:
        if i > 0:
            posi.append(i)
        else:
            negi.append(i)
    min_index = min(len(posi), len(negi))
    print(min_index)
    for i in range(min_index):
        nums[2 * i] = posi[i]
        nums[2 * i + 1] = negi[i]

    index = min_index * 2
    if len(posi) > len(negi):
        for j in range(len(negi), len(posi)):
            nums[index] = posi[j]
            index += 1
    else:
        for j in range(len(posi), len(negi)):
            nums[index] = negi[j]
            index += 1

    return nums


print(main([3, 1, -2, -5, 2, -4]))
print(main1([3, 1, -2, -5, 2, -4]))
print(main2([3, 1, -2, -5, 2, -4, -7]))
print(main2([-1, 2, 3, 4, -3, 1, 5, 7]))
