# find the nth root of the integer


def main(num, root):
    # brute force
    # tc - O(num * logroot) (in getting the pow it will take log root)

    for i in range(1, num):
        temp = i**root
        if temp == num:
            return i
        elif temp > num:
            break

    return -1


print(main(27, 3))
print(main(69, 4))

# binary search


def main1(num, root):

    # tc - O(logm) * O(logroot) # this O(logroot) is for mid**root
    low = 1
    high = num

    while low <= high:
        mid = low + ((high - low) // 2)

        if mid**root == num:
            return mid
        elif mid**root > num:
            high = mid - 1
        else:  # mid**root < num
            low = mid + 1

    return -1


print(main1(27, 3))
print(main1(69, 4))
