class HeapNode:
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return self.val < other.val


a = HeapNode(5)
b = HeapNode(10)

print(a < b)
