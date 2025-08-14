class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

A = Node(34)
B = Node(2)
C = Node(5)

A.next = B
B.next = C

head = A

def insert_node(head , data):
    new_node = Node(data)
    new_node.next = head
    head = new_node
    return head

def traverse(head):
    current = head
    while current is not None:
        print(current.data, end="->")
        current = current.next
    print("None")


head = insert_node(head, 45)


traverse(head)
