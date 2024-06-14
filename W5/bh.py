class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def Remove_n(head, n):
    prev = ListNode(0)
    prev.next = head
    first = prev
    second = prev
    
    for _ in range(n + 1):
        if second is None:  
            return None
        second = second.next
    
    while second is not None:
        first = first.next
        second = second.next
    
    first.next = first.next.next
    
    return prev.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

n = 3
result = Remove_n(head, n)

while result:
    # print(result.value, end=" ")
    print(result.value, end=" -> " if result.next else "\n")
    
    result = result.next
