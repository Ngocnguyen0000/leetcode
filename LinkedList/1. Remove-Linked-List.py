class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head, val):
    while head and head.val == val:
        head = head.next
    
    current = head
    prev = None
    
    while current:
        if current.val == val:
            prev.next = current.next
        else:
            prev = current
        current = current.next

    return head

def printLinkedList(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()

def createLinkedList(arr):
    dummy = ListNode()
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

head1 = createLinkedList([1,2,6,3,4,5,6])
val1 = 6
new_head1 = removeElements(head1, val1)
printLinkedList(new_head1)  # Output: 1 2 3 4 5

