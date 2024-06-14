class Solution:
    def FindMiddleNode(self, head):
        onestep = head
        twostep = head
        
        while twostep and twostep.next:
            onestep = onestep.next
            twostep = twostep.next.next
        # Trả về nút ở giữa
        return onestep 

    def CreateLinkedList(self, arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for value in arr[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

    def PrintLinkList(self, head):
        current = head
        result = []
        while current:
            result.append(current.val)
            current = current.next
        return result

solution = Solution()
head = solution.CreateLinkedList([1,2,3,4,5])
middle = solution.FindMiddleNode(head)
print(solution.PrintLinkList(head)) 

print(solution.PrintLinkList(middle))
