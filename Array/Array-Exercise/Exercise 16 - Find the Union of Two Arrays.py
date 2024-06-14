# class Solution:
#     def removeDuplicates(self, arr1, arr2):
#         # Chuyển đổi 2 mảng arr1 và arr2 thành tập hợp, những phần tử bị lặp lại sẽ bị loại bỏ
#         set1 = set(arr1) 
#         set2 = set(arr2)
#         # Phép hợp giữa 2 tập hợp
#         set3 = set1.union(set2)
#         return list(set3)
    
# solution = Solution()
# array1 = [1, 2, 3, 4]
# array2 = [3, 4, 5, 6]

# set3 = solution.removeDuplicates(array1, array2)
# print("The union of the sets is", set3)


class Solution:
    def union(self, arr1, arr2, arr3):
        # C1: 
        union_set = set(arr1)  
        for element in arr2:
            union_set.add(element)
        return list(union_set)
        
        
        # # C2: 
        # arr3 = set(arr1 + arr2)
        # return list(arr3)
        
        # C3:
        # union_list = list(arr1)
        # for element in arr2:
        #     if element not in union_list:
        #         union_list.append(element)
        
        # return union_list
        
    


            
        

        
                
solution = Solution()
array1 = [1, 2, 3, 4]
array2 = [3, 4, 5, 6]

result = solution.union(array1, array2)
print("The union is", result)



# class Solution:
#     def union(self, arr1, arr2):
        
