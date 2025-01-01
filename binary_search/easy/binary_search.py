# binary search always works on sorted data

# concept -> split the data into two halfs and check where u wanna go, left or right


# find the target in the arrray

def main(nums, target):
    # brute force
    # tc - O(n)
    # sc - O(1)
    for i in nums:
        if i == target:
            return True

    return False


def main1(nums, target):

    # binary search -iterative approach
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + ((high - low) // 2)

        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return False

def recursive_binary_search(arr, low, high, target):

    # base case
    if low > high:
        return False, -1 

    mid = low + ((high-low)//2)

    if arr[mid] == target:
        return True, mid
    elif arr[mid] > target:
        return recursive_binary_search(arr, low, mid-1, target)
    else:
        return recursive_binary_search(arr,mid+1, high,target)

def main2(nums, target):
    # we will use recurion here

    return recursive_binary_search(nums, 0, len(nums)-1, target)


print(main([2,3,4,7,8], 8))
print(main1([2,3,4,7,8], 8))
print(main2([2,3,4,7,8], 8))


# time complexity for iterative
# dividing by 2 
# tc - O(logn) log is base 2
# sc - O(1)