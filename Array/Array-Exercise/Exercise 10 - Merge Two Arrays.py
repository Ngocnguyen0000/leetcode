class Solution: 
    
    def mergeTwoArray(self, arr1, arr2): 
        result = arr1 + arr2
        return result

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
solution = Solution()
result = solution.mergeTwoArray(arr1, arr2)  
print("The merged array is:", result)
