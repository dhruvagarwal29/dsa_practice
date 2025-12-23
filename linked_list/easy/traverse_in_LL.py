# traverse in the array
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def convert_arr_to_ll(arr):
    head = Node(arr[0])
    mover = head
    for i in range(1, len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp

    return head


def length_of_LL(head):
    cnt = 0
    while head:
        cnt += 1
        head = head.next

    return cnt


def main():
    head = convert_arr_to_ll([1, 2, 3, 4, 5])
    # traversing LL's head
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")

    print("length of LL", length_of_LL(head))


main()
