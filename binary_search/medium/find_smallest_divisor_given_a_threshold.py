""" find the smallest divisor for the array whise sum after dividing all the elements 
are smaller or equal to threshold """


def sum_array(nums, divisor):
    total_sum = 0
    for num in nums:
        if num % divisor == 0:
            temp = num // divisor
        else:
            temp = (num // divisor) + 1

        total_sum += temp

    return total_sum


def main(nums, threshold):
    for num in range(1, max(nums) + 1):
        if sum_array(nums, num) <= threshold:
            return num


def main1(nums, thereshold):
    low = 1
    high = max(nums)

    while low <= high:
        mid = (low + high) // 2

        totl_sum = sum_array(nums, mid)

        if totl_sum <= thereshold:
            high = mid - 1
        else:
            low = mid + 1

    return low


print(main([1, 2, 5, 9], 6))
print(main([44, 22, 33, 11, 1], 5))

print(main1([1, 2, 5, 9], 6))
print(main1([44, 22, 33, 11, 1], 5))
