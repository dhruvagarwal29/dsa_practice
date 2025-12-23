# delete head from the doubly linked list


class Node:
    def __init__(self, data, next=None, back=None) -> None:
        self.data = data
        self.next = next
        self.back = back

    def __repr__(self) -> str:
        nxt = self.next.data if self.next else None
        bck = self.back.data if self.back else None

        return f"data = {self.data}, next = {nxt}, back = {bck}"


def create_doubly_linked_list(arr):

    head = Node(arr[0])
    prev = head

    for i in range(1, len(arr)):
        temp = Node(arr[i], None, back=prev)
        prev.next = temp
        prev = temp

    return head


def display_linked_list(head):
    while head:
        print(head)
        head = head.next


def delete_head_from_start(head):
    if not head or not head.next:
        return None

    new_head = head.next
    head.next = None
    new_head.back = None
    return new_head


def delete_tail(head):
    if not head or not head.next:
        return None

    curr = head
    while curr.next:
        curr = curr.next

    prev = curr.back
    prev.next = None
    curr.back = None

    return head


def delete_kth_element(head, k):
    if not head:
        return None
    if not head.next:
        return None

    temp = head
    cnt = 1

    while temp and cnt < k - 1:
        temp = temp.next
        cnt += 1

    prev = temp.back
    front = temp.next

    prev.next = front
    front.back = prev

    temp.back = None
    temp.next = None

    return head


def main():

    # display_linked_list(
    #     delete_head_from_start(create_doubly_linked_list([1, 2, 3, 4, 5]))
    # )

    # display_linked_list(delete_tail(create_doubly_linked_list([1, 2, 3, 4, 5])))
    display_linked_list(
        delete_kth_element(create_doubly_linked_list([1, 2, 3, 4, 5]), k=2)
    )


main()
