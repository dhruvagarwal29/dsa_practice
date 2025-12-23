# Painter's partition or Split array


def main(nums, k):
    low = max(nums)
    high = sum(nums)

    while low < high:
        mid = (low + high) // 2

        noofworkers = check_maximum(nums, mid)
        if noofworkers == k:
            return mid
        elif noofworkers > k:
            low = mid + 1
        else:
            high = mid - 1


def check_maximum(nums, mid):
    noofworkers = 1
    res = 0
    for i in nums:
        if i + res <= mid:
            res += i
        else:
            noofworkers += 1
            res = i

    return noofworkers


print(main([10, 20, 30, 40], 2))
