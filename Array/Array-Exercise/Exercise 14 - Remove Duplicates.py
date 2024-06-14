# class Solution:
#     def removeDuplicates(self, arr1):
#         # Chuyển đổi 2 mảng arr1 và arr2 thành tập hợp, những phần tử bị lặp lại sẽ bị loại bỏ
#         set1 = set(arr1) 
#         return list(set1)
    
# solution = Solution()
# arr1 = [1, 2, 3, 4, 3, 2, 1]

# set1 = solution.removeDuplicates(arr1)
# print("The union of the sets is", set1)


class Solution:
    def removeDuplicates(self, arr):
        new_arr = set()
        duplicates = set()
        
        for i in range(len(arr)):
            if arr[i] in new_arr:
                duplicates.add(arr[i])
            else:
                new_arr.add(arr[i])
        return list(new_arr)

solution = Solution()
arr = [1, 2, 3, 4, 3, 2, 1]

result = solution.removeDuplicates(arr)
print("The remove duplicates are", result)