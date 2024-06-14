# Nó được sử dụng để tìm kiếm một phần tử trong một mảng được sắp xếp
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return -1

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
#       
#      
#          
target = 5

result = binary_search(arr, target)

if result != -1:
    print("Phần tử", target, "được tìm thấy tại vị trí", result)
else:
    print("Phần tử", target, "không tồn tại trong mảng")
