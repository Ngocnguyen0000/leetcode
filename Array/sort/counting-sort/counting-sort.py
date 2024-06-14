class Solution:
    def sortArrayWithNElements(self, arr, N):
        # Tạo mảng đếm với kích thước N+1 để chứa số lượng xuất hiện của mỗi số từ 0 đến N.
        count = [0] * (N + 1)
        
        for num in arr:
            count[num] += 1
        # Xây dựng lại mảng đã sắp xếp từ mảng đếm
        index = 0
        for num in range(N + 1):
            while count[num] > 0:
                arr[index] = num
                index += 1
                count[num] -= 1 
        return arr

# Mã nguồn dùng thử
# arr = [3, 0, 2, 5, 4, 3, 1, 2, 1, 0, 5, 4, 3, 2]  # Khởi tạo mảng với các số từ 0 đến N
# N = 5  # Giá trị lớn nhất trong mảng

arr = [0, 2,0,1,2]  # Khởi tạo mảng với các số từ 0 đến N
# count[] = [2, 1,2]
# arrSort = [0 0 1 2 2]
N = 3  # Giá trị lớn nhất trong mảng

solution = Solution()
sorted_arr = solution.sortArrayWithNElements(arr, N)
print(sorted_arr)


# Thời gian: O(n + k), với n là số phần tử trong mảng và k là phạm vi của các số (từ 0 đến N).
# Không gian: O(k) để lưu mảng đếm.

# Trong counting sort, mảng đếm count lưu số lần xuất hiện của mỗi phần tử. Sau đó, sử dụng mảng đếm này để điền các phần tử vào mảng kết quả theo thứ tự đã sắp xếp.