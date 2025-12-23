# instead of printing all the subsequences, just print any of the subsequence with sum k


def any_subsequence(arr, k):

    # here we can use true and false in base condition

    result = []

    def backtrack(i, total, s):
        if i == len(arr):
            if s == k:
                result.append(list(total))
                return True
            else:
                return False

        if backtrack(i + 1, total + [arr[i]], s + arr[i]) == True:
            return True

        if backtrack(i + 1, total, s) == True:
            return True

        return False

    backtrack(0, [], 0)
    return result


print(any_subsequence([1, 2, 1], 2))
