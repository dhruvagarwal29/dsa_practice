class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return f"{self.data, self.next}"


def create_linked_list(arr):
    head = Node(arr[0])
    mover = head

    for i in range(1, len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp

    return head


# insert at the head
def insert_at_head(head, value):
    node = Node(value)
    node.next = head

    return node


# insert at tail
def insert_at_tail(head, value):
    node = Node(value)
    if not head:  # empty list case
        return node
    temp = head

    while temp.next:
        temp = temp.next

    temp.next = node
    return head


def insert_at_kth_element(head, k, val):

    if not head:
        return Node(val)

    if k == 1:
        node = Node(val)
        node.next = head
        return node

    temp = head
    cnt = 1
    while temp and cnt < k - 1:
        temp = temp.next
        cnt += 1

    node = Node(val)
    node.next = temp.next
    temp.next = node

    return head


def main():
    arr = [1, 2, 3, 4, 5]
    head = create_linked_list(arr)
    # print(head)
    # print(insert_at_head(head=head, value=9))
    # print(insert_at_tail(head=head, value=9))f
    print(insert_at_kth_element(head=head, k=5, val=9))
    print(insert_at_kth_element(head=head, k=2, val=9))
    print(insert_at_kth_element(head=head, k=6, val=9))


main()
