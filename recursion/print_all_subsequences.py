# print all consecutive subsequences of the array
# when it comes to all we need to use recursion


def subsequence(arr, index, result, total):

    if index >= len(arr):
        total.append(list(result))
        return

    result.append(arr[index])
    subsequence(arr, index + 1, result, total)
    result.pop()
    subsequence(arr, index + 1, result, total)


def main():
    arr = [3, 1, 2]
    total = []
    subsequence(arr, 0, [], total)
    return total


print(main())
