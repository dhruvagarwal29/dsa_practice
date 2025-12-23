# check the string is palindrome or not using recursion and iterative approach


# def itrative_palindrome(s):
#     l = 0
#     r = len(s) - 1

#     while l <= r:
#         if s[l] != s[r]:
#             return False
#         l += 1
#         r -= 1
#     return True


# def main():
#     s = "mom"
#     s1 = "madam"
#     s2 = "car"

#     print(itrative_palindrome(s))
#     print(itrative_palindrome(s1))
#     print(itrative_palindrome(s2))


# main()


# recursive way


def recursive_palindrome(s, l, r):

    if l >= r:
        return True

    if s[l] != s[r]:
        return False

    recursive_palindrome(s, l + 1, r - 1)


def main():
    # s = "madam"
    # return recursive_palindrome(s, 0, len(s) - 1)

    s1 = "car"
    return recursive_palindrome(s1, 0, len(s1) - 1)


print(main())
