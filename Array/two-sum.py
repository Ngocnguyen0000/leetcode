class Solution:
    def twoSum(self, nums, target):
        # Duyệt qua từng phần tử trong mảng
        for i in range(len(nums)):
            # Đối với mỗi phần tử, duyệt qua các phần tử tiếp theo
            for j in range(i + 1, len(nums)):
                # Kiểm tra nếu tổng của các phần tử tại chỉ số i và j bằng giá trị mục tiêu
                if nums[j] == target - nums[i]:
                    # Nếu điều kiện thỏa mãn, trả về các chỉ số
                    return [i, j]

# Driver code
nums = [2, 7, 11, 17]
target = 9

# Tạo một đối tượng của lớp Solution
solution = Solution()

# Gọi phương thức twoSum và in kết quả
print(solution.twoSum(nums, target))
