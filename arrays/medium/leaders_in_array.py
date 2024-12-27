# we need to find the leaders in array which means everything on the right of an element
# has to smaller than that
# arr = [10,22,12,3,0,6] ans = [22,12,6]
# cause evrything after 22 is smaller than 22, same with 12, but not with 3 as 6 > 3
# but 6 is also a leader as nothing after it


# brute force
# tc - O(n^2)
# sc - nothing to solve the problem, but to store the ans is O(n)


def main(nums):
    arr = []
    for i in range(len(nums)):
        leader = True
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                leader = False
                break

        if leader == True:
            arr.append(nums[i])

    return arr


# optimal solu
# we need to traverse the array in reverse loop


def main1(nums):
    # time complexity is O(n), sc = O(n)
    # could be O(nlogn) as question can ask for sorted ans
    maxi = float("-inf")
    arr = []
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] > maxi:
            maxi = nums[i]
            arr.append(maxi)

    return arr


print(main([10, 22, 12, 3, 0, 6]))
print(main1([10, 22, 12, 3, 0, 6]))
print(main1([5, 4, 3, 2, 1]))
