class Solution:
    def InsertHead(self, new_data):
        new_node = Node(new_data)  # Tạo một nút mới với dữ liệu mới
        new_node.next = self.head  # Đặt con trỏ next của nút mới trỏ tới đầu danh sách hiện tại
        self.head = new_node  # Cập nhật con trỏ head để trỏ tới nút mới, biến nó thành đầu danh sách mới
