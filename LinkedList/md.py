class ListNode:
    def __init__(self, value=0, next=None):  
        self.value = value
        self.next = next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

def mid_linked_list(head):
    if not head:  
        return None
    onestep = head
    twostep = head

    while twostep and twostep.next:
        onestep = onestep.next
        twostep = twostep.next.next
    return onestep

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next



middle_node = mid_linked_list(node1)
print(f"The middle button has value: {middle_node.value if middle_node else 'None'}")
