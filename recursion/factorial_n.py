# factorial of n is multiplication to n
# paramterised way


def fact(i, n):
    if i < 1:
        print(n)
        return

    fact(i - 1, n * i)


def main():
    fact(4, 1)


main()


# functional way


def fact1(n):
    if n == 1:
        return 1

    return n * fact1(n - 1)


print(fact1(5))
