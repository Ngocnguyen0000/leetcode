# class Node:
#     def _init_(self, data):
#         self.data   = data
#         self.next = None
    
# class LinkList:
#     def _init_(self):
#         self.head = None
        
#     def push
    
    
    
    def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    first = dummy
    second = dummy
    for _ in range(n + 1):
        first = first.next
    while first:
        first = first.next
        second = second.next
    second.next = second.next.next
    return dummy.next
