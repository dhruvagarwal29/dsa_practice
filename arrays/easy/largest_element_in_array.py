# find the largest element in array


def main(arr):
    # sorting will take nlogn time complexity
    arr.sort()
    return arr[-1]


def main1(arr):
    # better solution then above will take O(n) time complexity just traversing the
    # array and O(1) space
    max = 0

    for n in arr:
        if n > max:
            max = n

    return max


print(main([1, 3, 6, 2, 8, 8, 10, 4]))
print(main1([1, 3, 6, 2, 8, 8, 10, 4]))
