class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def getIntersectionNode(headA, headB):
        if not headA or not headB:
            return None

        pA = headA
        pB = headB


        while pA != pB:
            if pA is None:
                pA = headB
            else:
                pA = pA.next
            
            if pB is None:
                pB = headA
            else:
                pB = pB.next

        return pA


    def create_linked_list(values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head


    def print_linked_list(head):
        values = []
        while head:
            values.append(head.val)
            head = head.next
        print(" -> ".join(map(str, values)))

listA = Solution.create_linked_list([1, 2, 3, 4, 5])
#                                    pA 

listB = Solution.create_linked_list([6, 7, 8, 4, 5])
#                                    pB

intersection = listA.next.next.next
listB.next.next = intersection
result = Solution.getIntersectionNode(listA, listB)
if result:
    print(f"Intersected at '{result.val}'")
else:
    print("No intersection")
