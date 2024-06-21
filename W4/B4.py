class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

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
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

class Solution:
    def reverseList(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next  
            current.next = prev       
            prev = current            
            current = next_node       
        return prev

solution = Solution()

list = [2,1]
head = CreateLinkedList(list)
reversed_head = solution.reverseList(head)
PrintLinkedList(reversed_head)

