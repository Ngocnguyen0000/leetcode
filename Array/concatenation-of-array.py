from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []  # Hoặc bất kỳ giá trị nào khác bạn muốn trả về cho mảng rỗng
        return nums * 2

solution = Solution()

# Trường hợp mảng không rỗng
result = solution.getConcatenation([])
print(result)  # Kết quả: [1, 2, 1, 1, 2, 1]


