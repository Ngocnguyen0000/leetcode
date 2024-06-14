# tìm phần tử đc lặp lại

# arr[] = [2, 3, 1, 2, 3, 2, 1, 0]
# n=8
# Output: 1 2 3


class Solution:
    def duplicates(self, arr, n): 
        # Đầu tiên kiểm tra tất cả các giá trị có trong mảng, sau đó
        # sử dụng các giá trị này làm chỉ số và tăng giá trị tại các chỉ số này
        # bằng kích thước của mảng
        for i in range(0, n): 
            index = arr[i] % n 
            arr[index] += n 
    
        # Bây giờ kiểm tra giá trị nào xuất hiện nhiều hơn một lần
        # bằng cách chia giá trị tại các chỉ số này với kích thước của mảng
        check = False
        res = []
        for i in range(0, n): 
            if (arr[i] // n) > 1: 
                res.append(i)
                check = True
        
        # Nếu không có phần tử nào lặp lại, thêm -1 vào kết quả
        if check == False:
            res.append(-1)
        
        return res
	    