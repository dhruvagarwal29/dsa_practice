# merge 2 sorted arrays without using extra space

# if extra space can be used


def main(nums1, nums2):
    # brute force
    # tc - O(n+m) + O(n+m)
    # sc - O(n+m)
    a, b = 0, 0

    arr = []

    while a < len(nums1) and b < len(nums2):

        if nums1[a] <= nums2[b]:
            arr.append(nums1[a])
            a += 1
        else:
            arr.append(nums2[b])
            b += 1

    while a < len(nums1):
        arr.append(nums1[a])
        a += 1

    while b < len(nums2):
        arr.append(nums2[b])
        b += 1

    # putting this arr into nums1 and nums2
    for i in range(len(arr)):
        if i < len(nums1):
            nums1[i] = arr[i]
        else:
            nums2[i - len(nums1)] = arr[i]

    return arr, nums1, nums2


# we need to remove the extra space
# we will swap the largest element with samllest element in nums2 and sort


# a better sol
def main1(nums1, nums2):
    # tc - O(nlogn) + O(mlogm) + O(min(n,m))
    # sc - O(1)
    left = len(nums1) - 1
    right = 0

    while left >= 0 and right < len(nums2):  # or could be while True
        if nums1[left] > nums2[right]:
            nums1[left], nums2[right] = nums2[right], nums1[left]
            left -= 1
            right += 1
        else:
            break
    nums1.sort()
    nums2.sort()

    return nums1, nums2


# above is also optimal sol, we have another sol which is using gap method
# it will use shell sort


def main2(nums1, nums2):
    # this is a good sol
    # tc for first while loop as we are dividing the gap by 2 and so on till it is 1 -> O(log (n+m))
    # tc for inner loop O(n+m)
    # tc - O(log(n_m)) *O(n+m)
    # sc - O(1)
    tlen = len(nums1) + len(nums2)

    gap = (tlen // 2) + (tlen % 2)  # this is taking the ceil of divsion by 2

    while gap > 0:
        left = 0
        right = left + gap

        while right < tlen:
            if left < len(nums1) and right >= len(nums1):
                # means left in nums1 and right in nums2
                # nums1 and nums2
                swap(nums1, nums2, left, right - len(nums1))
            elif left >= len(nums1):  # means both pointers are in nums2
                # nums2 and nums2
                swap(nums2, nums2, left - len(nums1), right - len(nums1))

            else:
                swap(nums1, nums1, left, right)
                # both pointers are in nums1
            left += 1
            right += 1

        if gap == 1:
            break
        gap = (gap // 2) + (gap % 2)

    return nums1, nums2


def swap(nums1, nums2, i1, i2):
    if nums1[i1] > nums2[i2]:
        nums1[i1], nums2[i2] = nums2[i2], nums1[i1]


print(main([1, 3, 5, 6, 7], [0, 2, 6, 8, 9]))
print(main1([1, 3, 5, 6, 7], [0, 2, 6, 8, 9]))
print(main2([1, 3, 5, 6, 7], [0, 2, 6, 8, 9]))
