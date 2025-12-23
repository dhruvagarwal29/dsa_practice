# print all the subsequences whose sum is equal to k


# def subsequence_sum(arr, total, result, index, k):

#     if index == len(arr):
#         if sum(result) == k:
#             total.append(list(result))
#         return

#     result.append(arr[index])
#     subsequence_sum(arr, total, result, index + 1, k)
#     result.pop()
#     subsequence_sum(arr, total, result, index + 1, k)


# def main():
#     arr = [1, 2, 3]
#     k = 6
#     total = []
#     subsequence_sum(arr, total, [], 0, k)
#     return total


# print(main())


# another way of wrting this


def subsequence_sum(arr, k):
    total = []

    def backtrack(i, result, s):
        if i == len(arr):
            if s == k:
                total.append(list(result))
            return

        # include
        backtrack(i + 1, result + [arr[i]], s + arr[i])

        # not include
        backtrack(i + 1, result, s)

    backtrack(0, [], 0)
    return total


print(subsequence_sum([1, 2, 3], 6))
print(subsequence_sum([1, 2, 1], 2))
