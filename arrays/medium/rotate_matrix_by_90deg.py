# rotate matrix by 90deg


def main(nums):
    # brute force
    # tc = O(n^2)
    # sc = O(n^2)
    r = len(nums)
    c = len(nums[0])

    arr = [[0 for i in range(c)] for i in range(r)]

    for i in range(r):
        for j in range(c):
            arr[j][r - i - 1] = nums[i][j]

    return arr


# optimal sol - we need to optimize it on space parameter
# we need to transpose the matrix first and then reverse the rows


def main1(nums):
    # to transpose the matrix we just need to swap elements where i & j is not equal
    # tc = O(r/2*c/2) + O(n * n/2)
    #      for swapping, for reversing, first loop through array and then reverse
    # sc - O(1)
    r = len(nums)
    c = len(nums[0])

    for i in range(r):
        for j in range(i, c):
            if i != j:
                nums[i][j], nums[j][i] = nums[j][i], nums[i][j]

    for i in range(r):
        nums[i].reverse()

    return nums


print(main([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(main1([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
