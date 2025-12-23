# fibonacci series is the summation of first 2 numbers makking the third one

# 0,1,1,2,3,5,8


def fibo(n):

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibo(n - 1) + fibo(n - 2)


def main():

    arr = []

    for i in range(6):
        arr.append(fibo(i))

    print(arr)


main()

# time complexity is 2^n and space is N

# using array memoization


def fact1(n):
    arr = [0] * (n + 1)

    arr[1] = 1

    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
    print(arr)
    return arr[n]


print(fact1(5))
