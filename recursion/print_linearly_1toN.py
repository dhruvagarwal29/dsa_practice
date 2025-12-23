def print_1_to_N(start, N):
    if start == N + 1:
        return

    print(start)

    print_1_to_N(start + 1, N)


print_1_to_N(1, 9)


def print_N_to_1(N):
    if N == 0:
        return

    print(N)
    print_N_to_1(N - 1)


print_N_to_1(9)
