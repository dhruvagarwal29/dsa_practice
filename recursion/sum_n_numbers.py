# give the sum of n numbers using parameterised way and fucntional way

# parameterised way
# 1 to N


# def sum_n(total, count, n):

#     if count > n:
#         print(total)
#         return

#     sum_n(total + count, count + 1, n)


# def main():
#     sum_n(0, 0, 3)


# main()


# N to 1


# def sum_n(count, total):
#     if count < 1:
#         print(total)
#         return

#     sum_n(count - 1, total + count)


# def main():
#     sum_n(3, 0)


# main()


# fucntional way
# where function returns the sum


def sum_n(n):
    if n == 1:
        return 1

    return n + sum_n(n - 1)


def main():
    print(sum_n(3))


main()
