class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getIntersectionNode(headA, headB):
    if pA is None:
        pA = headB
    else:
        pA = pA.next
        
        # Nếu pB đến cuối danh sách B, chuyển nó đến đầu danh sách A
    if pB is None:
        pB = headA
    else:
        pB = pB.next

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Hàm trợ giúp để in danh sách liên kết
def print_linked_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(" -> ".join(map(str, values)))


listA = create_linked_list([1, 2, 3, 4, 5])
#                           pA 
listB = create_linked_list([6, 7, 8, 4, 5])
#                           pB

intersection = listA.next.next.next  
listB.next.next = intersection  


result = getIntersectionNode(listA, listB)


if result:
    print(f"Intersected at '{result.val}'")
else:
    print("No intersection")





