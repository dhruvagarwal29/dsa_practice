# find the union of sorted arrays


def main(nums1, nums2):
    s = set()
    # this is a brute force approach it will take O(nlogn) complexity
    # and O(n+m) space complexity worst case

    for i in range(len(nums1)):

        s.add(nums1[i])

    for i in range(len(nums2)):
        s.add(nums2[i])

    s = sorted(s)
    return s


def main1(nums1, nums2):
    # this will just work for sorted arrays not for unsorted arrays
    # time complexity = O(n) + O(n)
    # space complexity = O(n + n)
    n1 = 0
    n2 = 0
    arr = []

    while n1 < len(nums1) and n2 < len(nums2):
        if nums1[n1] <= nums2[n2]:
            if len(arr) == 0 or arr[-1] != nums1[n1]:
                arr.append(nums1[n1])
            n1 += 1
        else:
            if len(arr) == 0 or arr[-1] != nums2[n2]:
                arr.append(nums2[n2])
            n2 += 1

    while n1 < len(nums1):
        if arr[-1] != nums1[n1]:
            arr.append(nums1[n1])
        n1 += 1

    while n2 < len(nums2):
        if arr[-1] != nums2[n2]:
            arr.append(nums2[n2])
        n2 += 1

    return arr


print(main([4, 7, 2, 9, 1], [9, 1]))

print(main1([4, 7, 2, 9, 1], [9, 1]))  # will not work on this as it is unsorted array

print(main1([1, 2, 4, 5, 7], [1, 2, 3]))
