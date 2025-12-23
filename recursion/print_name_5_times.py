def print_name(count):
    if count == 5:
        return

    print("Ram")

    print_name(count + 1)


print_name(0)
