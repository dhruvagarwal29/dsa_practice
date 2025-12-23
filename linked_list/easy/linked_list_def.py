class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


def main():
    n = Node(5, 0)
    n2 = Node(6, n.data)
    print(n2)
    print(n2.next)
    print(n2.data)


main()
