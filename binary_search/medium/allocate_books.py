def find_students(arr_books, total_pages):

    student = 1
    student_pages = 0

    for i in arr_books:
        if i + student_pages <= total_pages:
            student_pages += i
        else:
            student += 1
            student_pages = i

    return student


def main(students, arr_books):

    low = max(arr_books)
    high = sum(arr_books)

    for i in range(low, high):

        stud = find_students(arr_books, i)

        if stud == students:
            return i


print(main(4, [25, 46, 28, 49, 24]))


def bianry_search(students, arr_books):
    low = max(arr_books)
    high = sum(arr_books)

    while low < high:
        mid = (low + high) // 2

        stud = find_students(arr_books, mid)

        if stud == students:
            return mid
        elif stud > students:
            low = mid + 1
        else:
            high = mid - 1


print(bianry_search(4, [25, 46, 28, 49, 24]))
