class Node:
    def __init__(self, data, next=None, back=None) -> None:
        self.data = data
        self.next = next
        self.back = back

    def __repr__(self) -> str:
        nxt = self.next.data if self.next else None
        bck = self.back.data if self.back else None
        return f"Node(data={self.data}, next={nxt}, back={bck})"


def convert_arr_to_dll(arr):

    head = Node(arr[0])
    prev = head

    for i in range(1, len(arr)):
        temp = Node(arr[i], None, back=prev)
        prev.next = temp
        prev = temp

    return head


def main():
    arr = [1, 2, 3, 4, 5]
    head = convert_arr_to_dll(arr)
    while head:
        print(head)
        head = head.next


main()
