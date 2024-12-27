# set the rows and columns to be zeroes where in matrix it is given as zeroes


def main(nums):
    # brute force
    # helper functions (just marking rows and cols as -1)
    # tc - O(n*m) * O(n+m) + O(n+m) -> first o(n*m) is to loop over the arrays and m+n
    # is to mark col and rows as -1 and the addition of m+n is cause we are iterating
    # over them again and changing them to zero
    # sc - O(1) we are not useing any extra space
    # finally its tc is O(n^3)
    def markRow(i):
        for j in range(c):
            if nums[i][j] != 0:
                nums[i][j] = -1

    def markCol(j):
        for i in range(r):
            if nums[i][j] != 0:
                nums[i][j] = -1

    r = len(nums)
    c = len(nums[0])

    # we need to mark row and columns which has zero in them

    for i in range(r):
        for j in range(c):
            if nums[i][j] == 0:
                markRow(i)
                markCol(j)

    for i in range(r):
        for j in range(c):
            if nums[i][j] == -1:
                nums[i][j] = 0

    return nums


# better solution
# we will not mark the element as -1 on the fly, we will just save the rows, cols
# in a seperate set


def main1(nums):
    # this is a better solution
    # tc = O(r*c) + O(r+c)
    # sc = O(r) + O(c)
    r = len(nums)
    c = len(nums[0])

    row_set = set()
    col_set = set()

    for i in range(r):
        for j in range(c):
            if nums[i][j] == 0:
                row_set.add(i)
                col_set.add(j)

    for i in range(r):
        for j in range(c):
            if i in row_set or j in col_set:
                nums[i][j] == 0

    return nums


# optimal solution- to minimize space
# we cannot change the reduce the time complexity as min time to traverse a matrix
# will take n^2 time, so will optimize the time complexity


def main2(nums):
    # we will replace those sets with row0 and col0, and we need a variable
    # to save the state of nums[0][0]

    is_col = False
    n = len(nums)
    m = len(nums[0])
    for i in range(n):
        if nums[i][0] == 0:
            is_col = True
        for j in range(1, m):
            if nums[i][j] == 0:
                nums[i][0] = 0
                nums[0][j] = 0

    for i in range(1, n):
        for j in range(1, m):
            if nums[i][j] != 0:
                if nums[i][0] == 0 or nums[0][j] == 0:
                    nums[i][j] = 0

    if nums[0][0] == 0:
        for j in range(m):
            nums[0][j] = 0

    if is_col:
        for i in range(n):
            nums[i][0] = 0

    return nums


# I gave nums as 3 times cause after getting it changed by main, it get changed
# for all others too cause list passes by reference

nums = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
print(main(nums))
nums = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
print(main1(nums))
nums = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
print(main2(nums))
