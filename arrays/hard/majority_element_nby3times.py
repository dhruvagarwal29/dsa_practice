# majority element appears in array more than n/3 times

# one observation is , there can be 2 elements which can appear in ana array n/3 times
# this is true for any size of array
# for eg : we have arr = [1,1,1,2,2,3,3,3] -> here len is 8-> n//3 = 2 > 2 ==> 3
# so element should be more than 2 times that is 3 times appear in the array
# there are only 2 elements which is 1,3 - at max 2 elemets are only present in any
# array which appears more than n//3 times
# min can be 0, when all elements are unique


def main(nums):
    # brute force
    # tc - O(n^2)
    # sc - O(n)
    ans = []  # now we know our ans can be only of lenght 2
    for i in range(len(nums)):
        if nums[i] not in ans and len(ans) != 2:
            cnt = 0
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    cnt += 1

            if cnt > len(nums) // 3:
                ans.append(nums[i])

    return ans


# better sol is through hashing
def main1(nums):
    # two pass
    # tc - O(2n)
    # sc - O(2n)
    hashmap = {}
    ans = []
    for i in nums:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1

    for k, v in hashmap.items():
        if v > len(nums) // 3:
            ans.append(k)

    return ans


def main2(nums):
    # one pass
    # tc - O(N)
    # sc - O(2N)
    hashmap = {}
    ans = []
    for i in nums:
        if i in hashmap:
            hashmap[i] += 1
            if hashmap[i] > len(nums) // 3:
                ans.append(i)
        else:
            hashmap[i] = 1

    return ans


# optimal solution


# for > n//2 times the algo is moore's voting algo
def greater_n_by_2_times(nums):
    cnt = 0
    el = 0

    for i in range(len(nums)):

        if cnt == 0:
            cnt = 1
            el = nums[i]
        elif nums[i] == el:
            cnt += 1
        else:
            cnt -= 1

    return el


# for n//3 times we need to modify the above algo only, the concept will be same
# but for two numbers and 2 extra checks


def main3(nums):
    # tc - O(n)
    # sc - O(1) for variables only

    cnt1, cnt2 = 0, 0
    # two variables as we know majority elements will be 2 if they are
    ele1, ele2 = -1, -1

    for i in range(len(nums)):
        if cnt1 == 0 and nums[i] != ele2:
            # some extra checks so that if ele1 is 1 then ele2 is not 1 again
            cnt1 = 1
            ele1 = nums[i]
        elif cnt2 == 0 and nums[i] != ele1:
            cnt2 = 1
            ele2 = nums[i]
        elif nums[i] == ele1:
            cnt1 += 1
        elif nums[i] == ele2:
            cnt2 += 1
        else:
            cnt1 -= 1
            cnt2 -= 1

    # print(cnt1, cnt2)

    # now here the algo finishes but we can check it manually

    c1, c2 = 0, 0
    for i in range(len(nums)):
        if ele1 == nums[i]:
            c1 += 1
        if ele2 == nums[i]:
            c2 += 1
    arr = []
    if c1 > len(nums) // 3:
        arr.append(ele1)
    if c2 > len(nums) // 3:
        arr.append(ele2)

    return ele1, ele2, arr


print(main([1, 1, 1, 3, 3, 3, 2, 2]))
print(main1([1, 1, 1, 3, 3, 3, 2, 2]))
print(main2([1, 1, 1, 3, 3, 3, 2, 2]))
print(main3([1, 1, 1, 3, 3, 3, 2, 2]))
print(greater_n_by_2_times([1, 1, 1, 1, 1, 3, 2, 2]))
