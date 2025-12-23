# iterative reversal of array using two pointers


# def reverse(arr):

#     l = 0
#     r = len(arr) - 1

#     while l != r:

#         arr[l], arr[r] = arr[r], arr[l]
#         l += 1
#         r -= 1

#     return arr


# print(reverse([1, 2, 3, 4, 5]))


# we have to do it using recursion


# # recursion using two pointers
# def reverse_recursion(arr, l, r):
#     if l >= r:
#         return

#     arr[l], arr[r] = arr[r], arr[l]

#     reverse_recursion(arr, l + 1, r - 1)


# def main():
#     arr = [1, 2, 3, 4, 5]
#     reversed_arr = reverse_recursion(arr, 0, len(arr) - 1)
#     print(reversed_arr)


# main()


# using single pointer/variable


def iterative_reverse(arr):
    n = len(arr) - 1

    for i in range(len(arr)):
        if i > n // 2:
            break
        arr[i], arr[n - i] = arr[n - i], arr[i]

    return arr


print(iterative_reverse([1, 2, 3, 4, 5]))


# recursive using 1 pointer


def recursive_reverse(arr, l):
    n = len(arr)
    while l >= (n // 2):
        return

    arr[l], arr[n - l - 1] = arr[n - l - 1], arr[l]
    recursive_reverse(arr, l + 1)


def main1():
    arr = [1, 2, 3, 4, 5]
    recursive_reverse(arr, 0)
    print(arr)


main1()
