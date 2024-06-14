class Solution:
    # Tạo phương thức đảo mảng/ 1 phần của mảng 
    def reverse(arr, start, end):
        while start < end:
            # Hoán đổi giá trị giữa arr[start] và arr[end]
            tmp = arr[start]
            arr[start] = arr[end]
            arr[end] = tmp
            
            start += 1
            end -= 1

    def rotate_array(arr, arr, position):
        n = len(arr)
        k = k % n  # Điều chỉnh k nếu nó lớn hơn n

        # Đảo ngược toàn bộ mảng --> [5 4 3 2 1]
        reverse(arr, 0, n - 1)
        # Đảo ngược phần đầu của mảng (từ 0 đến k - 1) --> [4 3 3 2 1]
        reverse(arr, 0, k - 1)
        # Đảo ngược phần cuối của mảng (từ k đến n - 1) --> [4 3 1 2 3]
        reverse(arr, k, n - 1)
        
        return arr

solution = Solution()
arr = [1, 2, 3, 4, 5]
#      i=0 --> 
#  5 4 3 2 1
#  4 5 3 2 1
#  4 5 1 2 3


position = 2
result = rotate_array(arr, k)

print("The array after rotating",k,"positions to the right is", result)
