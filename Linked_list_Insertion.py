class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


A = Node(2)
B = Node(3)
C = Node(4)


A.next = B
B.next = C


def Traverse(head):
    current = head
    while current is not None:
        print(current.data , end="->")
        current = current.next
        
head = A

Traverse(head)
