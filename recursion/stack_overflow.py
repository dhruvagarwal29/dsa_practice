## maximum recursion depth will be reached


def print_stack():
    print("1")
    print_stack()


def main():
    print_stack()


# main()


# solution we need a breaking condition to come out of recursion


def print_stack1(count):
    if count == 5:  # breaking condition or base condition
        return
    print("1")
    print_stack1(count + 1)


def main1():
    print_stack1(0)


main1()
