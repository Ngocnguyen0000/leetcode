class Solution:
    
    def sort01234(self, arr, n):
        left = 0         # Vị trí tiếp theo để đặt 0
        mid1 = 0         # Vị trí tiếp theo để đặt 1
        mid2 = 0         # Vị trí tiếp theo để đặt 2
        right = n - 1    # Vị trí tiếp theo để đặt 3
        far_right = n - 1 # Vị trí tiếp theo để đặt 4
        
        # Traverse the array with five pointers
        while mid2 <= right:
            if arr[mid2] == 0:
                arr[left], arr[mid2] = arr[mid2], arr[left]
                if left == mid1:
                    mid1 += 1
                if mid1 == mid2:
                    mid2 += 1
                left += 1
            elif arr[mid2] == 1:
                arr[mid1], arr[mid2] = arr[mid2], arr[mid1]
                if mid1 == mid2:
                    mid2 += 1
                mid1 += 1
            elif arr[mid2] == 2:
                mid2 += 1
            elif arr[mid2] == 3:
                arr[mid2], arr[right] = arr[right], arr[mid2]
                right -= 1
            else:  # arr[mid2] == 4
                arr[right], arr[far_right] = arr[far_right], arr[right]
                far_right -= 1
                if right > mid2:
                    right -= 1

# Mã nguồn dùng thử
arr = [0, 3, 1, 2, 4, 3, 0, 2, 1, 4]  # Khởi tạo mảng với các số 0, 1, 2, 3, 4
n = len(arr)  # Lấy độ dài của mảng

# Tạo một đối tượng của lớp Solution
solution = Solution()

# Gọi phương thức sort01234 để sắp xếp mảng
solution.sort01234(arr, n)

# In ra mảng đã được sắp xếp
print(arr)
