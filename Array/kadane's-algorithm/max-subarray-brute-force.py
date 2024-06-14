def max_subarray_brute_force(arr):

    
    
    
    for i in range(n):
        for j in range(i, n):
            current_sum = sum(arr[i:j+1])
            if current_sum > max_sum:
                max_sum = current_sum
                start, end = i, j
                
    return max_sum, arr[start:end+1]

# Ví dụ sử dụng
arr = [1, -3, 2, 1, -1, 3, -2, 3]
max_sum, subarray = max_subarray_brute_force(arr)
print(f"Tổng lớn nhất của mảng con: {max_sum}")
# print(f"Mảng con: {subarray}")



# Đánh giá hiệu suất:
# Độ phức tạp thời gian: O(n^3)
# - Hai vong lap long nhay co do phức tap la O(n^2)
# - Tính tổng của mỗi mảng con tốn O(n)