def print_1toN_backtrack(N):
    if N == 0:
        return
    print_1toN_backtrack(N - 1)
    print(N)


# print_1toN_backtrack(5)


def print_Nto1_backtrack(temp, N):
    if temp == N + 1:
        return
    print_Nto1_backtrack(temp + 1, N)
    print(temp)


print_Nto1_backtrack(0, 5)
