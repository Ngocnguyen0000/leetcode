def kadane_algorithm(arr):
    # max-sum: lưu trữ tông lớn nhất dã tìm thấy
    max_sum = arr[0] 
    # max-current lưu trũ tổng con lớn nhất đang xét
    max_current_sum = arr[0]

    for i in range(1, len(arr)):
        x = arr[i]        
        if x > max_current_sum + x:
            max_current_sum = x
        else:
            max_current_sum += x
        # So sánh tông lớn nhất ? tông đang xet
        if max_current_sum > max_sum:
            max_sum = max_current_sum

    return max_sum

# Ví dụ sử dụng
arr = [-2 , 3, 2, -1]
max_sum = kadane_algorithm(arr)
print(f"Tổng lớn nhất của mảng con: {max_sum}")
