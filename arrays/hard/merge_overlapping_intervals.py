# merge all overlapping subintervals


# brute force
def main(nums):
    # first sort
    # tc -> ~ <O(n^2)
    # sc - O(n)
    nums.sort()
    ans = []
    for a, b in nums:
        first_element = a
        second_element = b
        if len(ans) != 0 and ans[-1][1] >= second_element:
            continue
        for i, j in nums[1:]:

            if second_element > i:
                second_element = max(j, b)
            else:
                break
        ans.append([first_element, second_element])

    return ans


def main1(nums):
    # we will use one pass in it
    # we will check on the fly if the next list is part of the ans
    # tc - O(nlogn) + O(n)
    # sc - O(n)

    ans = []

    for a, b in nums:
        if len(ans) == 0 or a > ans[-1][1]:
            ans.append([a, b])
        else:
            ans[-1][1] = max(ans[-1][1], b)

    return ans


print(main([[1, 3], [2, 6], [8, 9], [9, 11], [8, 10], [2, 4], [15, 18], [16, 17]]))
print(main1([[1, 3], [2, 6], [8, 9], [9, 11], [8, 10], [2, 4], [15, 18], [16, 17]]))
