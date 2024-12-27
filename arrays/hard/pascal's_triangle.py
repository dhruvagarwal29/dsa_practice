# we have 3 types of questions in pascal's triangle
# 1) give row and column give me the element
# 2) print any nth row of pascal's traingle
# 3) given n, print the entire pascal triangle


##
# 1) part is simple we have formula for this, use combination formula
# nCr = n!/(r!) * (n-r)! \
# using above formula we can find the element, we have to do n as (r-1) and r as (c-1)
# to find the element
# so Ques-> find the element at row= 3 and column = 2
def factorial(num):
    fact = 1
    while num != 0:
        fact = fact * num
        num -= 1

    return fact


def main(row, col):
    # brute force

    n = row - 1  # this is the only way, whatever row and col is given just do -1
    r = col - 1

    # nCr = n! / (r) ! * (n-r)!

    n_fact = factorial(n)
    r_fact = factorial(r)
    n_r_fact = factorial(n - r)

    element = n_fact // ((r_fact) * (n_r_fact))

    return element


# better solution as we know (n-r)! comes in n! so we wont compute it as it is going to
# be cancelled out


def nCr(n, r):
    numerator = 1
    denominator = 1
    while r > 0:
        numerator *= n
        n -= 1
        denominator *= r
        r -= 1

    return numerator // denominator


# another way of finding nCr
def nCr1(n, r):
    res = 1
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)

    return res


# print(nCr(4, 2))
# print(nCr1(4, 2))
# print(main(5, 3))


## second type of problem - to print the nth row of pascal triangle

# as from above sol we can find the element which takes tc of O(r)
# we can use the same formula and find the nth row of pascal triangle by just
# change the r in nCr formula


def nth_row_pascal_traingle(n):
    arr = []
    # tc - O(n * r)
    # sc - O(n)
    for i in range(n):
        element = nCr(n - 1, i)
        arr.append(element)

    return arr


# we need to optimize the time here
def nth_row_pascal_traingle1(n):
    arr = []
    ans = 1
    arr.append(ans)

    for i in range(1, n):
        ans = (ans * (n - i)) // i
        arr.append(ans)

    return arr


# print(nth_row_pascal_traingle(6))
# print(nth_row_pascal_traingle1(6))


## third type is print entire pascal's triangle


def pascal(n):
    ans = []
    # tc = O(n^3)
    # sc = O*(n)

    for i in range(1, n + 1):
        elem = []
        res = 0
        for j in range(1, i + 1):
            res = nCr(i - 1, j - 1)
            elem.append(res)

        ans.append(elem)

    return ans


# generate row function
def generate_row_number(row):
    arr = []
    ans = 1
    arr.append(ans)

    for i in range(1, row):
        ans = (ans * (row - i)) // i
        arr.append(ans)

    return arr


def pascal1(n):
    pascal = []

    for i in range(1, n + 1):
        res = generate_row_number(i)
        pascal.append(res)

    return pascal


print(pascal(4))
print(pascal1(4))
print(generate_row_number(6))
