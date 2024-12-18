# intesection of 2 arrays - means elements present in both arrays, can be duplicates


def main(nums1, nums2):
    # brute force, time complexity - O(n^2)
    # space = O(n)
    visited = [0] * min(len(nums1), len(nums2))
    ans = []
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] == nums2[j] and visited[j] == 0:
                ans.append(nums1[i])
                visited[j] = 1
                break
            if nums2[j] > nums1[i]:
                break

    return ans


def main1(nums1, nums2):
    n1 = 0
    n2 = 0
    ans = []
    while n1 < len(nums1) and n2 < len(nums2):

        if nums1[n1] < nums2[n2]:
            n1 += 1
        elif nums1[n1] > nums2[n2]:
            n2 += 1
        else:
            ans.append(nums1[n1])
            n1 += 1
            n2 += 1

    return ans


print(main([1, 2, 2, 1], [2, 2]))
print(main1([1, 2, 2, 1], [2, 2]))
