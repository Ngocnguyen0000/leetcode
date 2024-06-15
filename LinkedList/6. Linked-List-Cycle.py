
class ListNode:
    def __init__(self, data):
        self.val = data
        self.next = None

def CreateLinkedList(new_list):
    if not new_list:
        return None
    head = ListNode(new_list[0])
    current = head
    for value in new_list[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def PrintLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next

class Solution_TwoPoint:
    def hasCycle(self, head):
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False




class Solution_Set:

    def hasCycle2(self, head: ListNode) -> bool:
        seen = set()
        cur = head

        while cur:
            if cur in seen:
                return True
            seen.add(cur)
            cur = cur.next

        return False


new_list = [2, 3, 4]
head = CreateLinkedList(new_list)

if head and head.next:
    head.next.next = head 

solution = Solution_TwoPoint()
result = solution.hasCycle(head)
print(result)
