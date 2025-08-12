class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

A = Node(34)
B = Node(23)
C = Node(67)

A.next = B
B.next = C

Head = A
new_node = Node(5678967)

while Head.next != None:
    Head = Head.next

Head.next = new_node

current = A
while current:
    print(current.data)
    current = current.next
