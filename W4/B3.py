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
        
# Solution1
class Solution1:
    def MergeSoft1(self, list1, list2):
        new_list = []
        for i in range(len(list1)):
            new_list.append(list1[i])
        for i in range(len(list2)):
            new_list.append(list2[i])
        return new_list
    
    def Arrange1(self, new_list):
        new_list.sort()
        return new_list

# Solution2
class Solution2:
    def MergeSoft2(self, list1, list2):
        for i in range(len(list1)):
            list2.append(list1[i])
        return list2
    
    def Arrange2(self, list2):
        list2.sort()
        return list2

# Solution3
# class Solution3:
#     def MergeSoft3(self, list1, list2):
#         seen = set()
#         new_list = list1 + list2
#         for item in new_list:
#             if item in seen:
#                 return True
#             seen.add(item)
#         return False

# Solution 4:
class Solution4:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        current = dummy
        while list1 and list2:
            if list1.value < list2.value:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        return dummy.next

solution = Solution1()

list1 = [2,1,4]
list2 = [1,2,4]

merged_list = solution.MergeSoft1(list1, list2)
arranged_list = solution.Arrange1(merged_list)
linked_list = CreateLinkedList(arranged_list)

# linked_list1 = CreateLinkedList(list1)
# linked_list2 = CreateLinkedList(list2)
# merged_linked_list = solution.mergeTwoLists(linked_list1, linked_list2)

# PrintLinkedList(merged_linked_list)
if linked_list is None:
    print("None")
else:
    PrintLinkedList(linked_list)



