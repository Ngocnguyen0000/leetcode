
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

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = 0
        while head:
            num = num * 2 + head.val
            head = head.next
        return num
    

new_list = [1,0,1]
head = CreateLinkedList(new_list)
solution = Solution()
result = solution.getDecimalValue(head)
print(result)

