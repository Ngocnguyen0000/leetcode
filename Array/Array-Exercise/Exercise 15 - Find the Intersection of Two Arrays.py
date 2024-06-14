# class Solution:
#     def intersection(self, arr1, arr2):
#         # Chuyển đổi 2 mảng arr1 và arr2 thành tập hợp thì nhưngx phần tử đc lặp lại sẽ bị loại bỏ lun
#         set1 = set(arr1) 
#         set2 = set(arr2)
#         # Chuyển đôỉ thành danh sách
#         # set1.intersection(set2): phép giao giữa 2 tập hợp
#         return list(set1.intersection(set2))
    
# solution = Solution()
# array1 = [1, 2, 3, 4]
# array2 = [3, 4, 5, 6]

# result = solution.intersection(array1, array2)
# print("The intersection is", result)


class Solution:
    def intersection(self, arr1, arr2):
        intersection_set = set()
        set_arr1 = set(arr1)
        for arr1[i] in arr2:
            if element in set_arr1:
                intersection_set.add(element)
        return list(intersection_set)
                
solution = Solution()
array1 = [1, 2, 3, 4]
array2 = [3, 4, 5, 6]

result = solution.intersection(array1, array2)
print("The intersection is", result)

        
    

# array1 = [1, 2, 3, 4]
# array2 = [3, 3,  4, 5, 6]
#           i  i 

# new_arr=[3,4]
# for i in 