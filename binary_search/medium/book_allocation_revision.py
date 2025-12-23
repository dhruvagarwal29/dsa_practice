# arr = [25,46,28,49,24]


def main(books, students):

    for i in range(max(books), sum(books)):

        if student_count(i, books) == students:
            return i


def binary_search(books, students):
    if len(books) < students:
        return -1

    low = max(books)
    high = sum(books)

    while low <= high:
        mid = low + ((high - low) // 2)
        student_cnt = student_count(mid, books)
        if student_cnt == students:
            return mid
        elif student_cnt > students:
            low = mid + 1
        else:
            high = mid - 1


def student_count(page, books):
    no_of_students = 1
    cnt = 0
    for pg in books:
        if cnt + pg <= page:
            cnt += pg
        else:
            no_of_students += 1
            cnt = pg

    return no_of_students


print(main([25, 46, 28, 49, 24], 4))
print(binary_search([25, 46, 28, 49, 24], 4))
