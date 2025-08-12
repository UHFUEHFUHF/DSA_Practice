class Node:
    def __init__(self , data):
        self.data = data
        self.next = None


A = Node(1)
B = Node(5)
C = Node(8)

A.next = B
B.next = C

current = A

def insert_atfirst(head , data):
    new_node = Node(data)
    new_node.next = head
    head = new_node
    return head


current = insert_atfirst(current , 24)

while current != None:
    print(current.data)
    current = current.next
