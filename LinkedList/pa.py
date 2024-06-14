class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Problem:
    def reverse(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

    def isPalindrome(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        reversed_second_half = self.reverse(slow)
        
        while reversed_second_half:
            if head.val != reversed_second_half.val:
                return False
            head = head.next
            reversed_second_half = reversed_second_half.next
        return True

    def areListsEqual(self, head1, head2):
        while head1 and head2:
            if head1.val != head2.val:
                return False
            head1 = head1.next
            head2 = head2.next
        return head1 == head2 == None

# Ví dụ sử dụng
problem = Problem()

# Tạo danh sách 1
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(2)
head1.next.next.next = ListNode(1)



def checkPalidrome(){
    
    
}