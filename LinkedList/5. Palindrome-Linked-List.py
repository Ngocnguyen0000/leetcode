# class ListNode:
#     def __init__(self, value=0, next=None):
#         self.value = value
#         self.next = next    

# node1 = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(2)
# node4 = ListNode(1)

# node1.next = node2
# node2.next = node3
# node3.next = node4

# head = node1

# def reverse_linked_list(head):
#     prev = None
#     current = head
#     while current is not None:
#         next_node = current.next
#         current.next = prev
#         prev = current
#         current = next_node
#     return prev

# def compare_linked_lists(head1, head2):
#     while head1 and head2:
#         if head1.value != head2.value:
#             return False
#         head1 = head1.next
#         head2 = head2.next
#     return head1 is None and head2 is None

# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def copy_linked_list(head):
#     if head is None:
#         return None
#     new_head = ListNode(head.value)
#     current_new = new_head
#     current_old = head.next
#     while current_old is not None:
#         current_new.next = ListNode(current_old.value)
#         current_new = current_new.next
#         current_old = current_old.next
#     return new_head

# copy_head = copy_linked_list(head)
# reversed_head = reverse_linked_list(head)

# print("Danh sách đã đảo ngược:")
# print_linked_list(reversed_head)

# # So sánh danh sách ban đầu và danh sách đã đảo ngược
# if compare_linked_lists(copy_head, reversed_head):
#     print("True")
# else:
#     print("False")
    
    
    
    
    
    
    
    
    
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
