# print the matrix in the spiral form

# there is no other sol then this, this is the optimal solution only


def main(nums):

    # tc = O(n*m)
    # sc = O(n*m)

    r = len(nums)
    c = len(nums[0])
    ans = []
    # we need 4 directions, to move first we will go right -> bottom -> left -> top
    top = 0
    bottom = r - 1
    left = 0
    right = c - 1

    while top <= bottom and left <= right:

        # 1st iteration left -> right

        for i in range(left, right + 1):
            ans.append(nums[top][i])

        top += 1  # means we got the first row

        # 2nd iteration top to bottom
        for i in range(top, bottom + 1):
            ans.append(nums[i][right])

        right -= 1  # we get the last column so just -ve the right pointer

        # 3rd iteration right to left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                ans.append(nums[bottom][i])

            bottom -= 1  # as we are done with last row

        # 4th iteration bottom to top
        if left <= right:
            for i in range(bottom, top - 1, -1):
                ans.append(nums[i][left])

            left += 1

    return ans


print(main([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
