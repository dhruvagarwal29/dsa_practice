# tc - O(n)


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return f"{self.data, self.next}"


def convert_arr_to_LL():
    arr = [2, 3, 4, 5]
    head = Node(arr[0])
    mover = head

    for i in range(1, len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp

    return head


def main():
    head = convert_arr_to_LL()

    while head:
        print(head)
        head = head.next


main()
