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

# Giải pháp 1
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

# Giải pháp 2
class Solution2:
    def MergeSoft2(self, list1, list2):
        for i in range(len(list1)):
            list2.append(list1[i])
        return list2
    
    def Arrange2(self, list2):
        list2.sort()
        return list2

# Giải pháp 3: Sử dụng tập hợp (set) để kiểm tra vòng lặp
class Solution3:
    def MergeSoft3(self, list1, list2):
        seen = set()
        new_list = list1 + list2
        for item in new_list:
            if item in seen:
                return True
            seen.add(item)
        return False

# Giải pháp 4: Gộp hai danh sách liên kết đã sắp xếp
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

# Khởi tạo đối tượng solution từ lớp Solution1, Solution2, Solution3 hoặc Solution4
# solution = Solution1()
# solution = Solution2()
solution = Solution4()

# Danh sách 1 và 2
list1 = [0, 2, 4]
list2 = [1, 3, 4]

# Gộp hai danh sách sử dụng Solution1 hoặc Solution2
# merged_list = solution.MergeSoft1(list1, list2)
# arranged_list = solution.Arrange1(merged_list)
# Tạo danh sách liên kết từ danh sách đã sắp xếp
# linked_list = CreateLinkedList(arranged_list)

# Hoặc gộp và sắp xếp danh sách liên kết sử dụng Solution4
linked_list1 = CreateLinkedList(list1)
linked_list2 = CreateLinkedList(list2)
merged_linked_list = solution.mergeTwoLists(linked_list1, linked_list2)

# In danh sách liên kết đã gộp và sắp xếp
PrintLinkedList(merged_linked_list)
