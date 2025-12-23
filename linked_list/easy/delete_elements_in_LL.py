class Node:
    def __init__(self, data, next=None):
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


def display_linked_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print("None")


# delete the head of the LL
def delete_head(head):
    if head:
        return head.next
    else:
        return None


# delete tail of the LL
def delete_tail(head):
    if not head and not head.next:
        return None

    temp = head

    while temp:
        if temp.next.next == None:
            temp.next = temp.next.next
        temp = temp.next
    return head


# delete kth element from the LL, k is the position given to u
def delete_kth_position(head, k):
    if not head:
        return head

    if k == 1:
        return head.next

    cnt = 1
    temp = head

    while temp and temp.next:
        cnt += 1
        if cnt == k:
            temp.next = temp.next.next
            break
        temp = temp.next

    return head


# # delete the element
# def delete_element_LL(head, element):
#     temp = head
#     prev = None

#     while temp:
#         if temp.data == element:
#             prev.next = prev.next.next
#             break

#         prev = temp
#         temp = temp.next

#     return head


# delete kth position - better way to delete it


def delete_element_LL(head, k):
    if not head:
        return None

    if k == 1:  # remove head
        return head.next

    temp = head
    cnt = 1
    while temp and cnt < k - 1:  # finding count and temp position
        temp = temp.next
        cnt += 1

    if temp and temp.next:
        temp.next = temp.next.next

    return head


def main():
    arr = [1, 2, 3, 4, 5]
    head = create_linked_list(arr)
    # display_linked_list(delete_head(head))  # 2 3 4 5 None
    # display_linked_list(delete_tail(head))  # 1 2 3 4 None
    # display_linked_list(delete_kth_position(create_linked_list(arr), 1))
    # display_linked_list(delete_kth_position(create_linked_list(arr), 2))
    # display_linked_list(delete_kth_position(create_linked_list(arr), 3))
    # display_linked_list(delete_kth_position(create_linked_list(arr), 5))
    # display_linked_list(delete_element_LL(create_linked_list([1, 4, 6, 9]), 9))

    display_linked_list(delete_kth_position(create_linked_list(arr), 1))
    display_linked_list(delete_kth_position(create_linked_list(arr), 2))
    display_linked_list(delete_kth_position(create_linked_list(arr), 3))
    display_linked_list(delete_kth_position(create_linked_list(arr), 5))


main()
