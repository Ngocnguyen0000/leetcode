class Solution:
    def IntersectionTwoArrays1(self, arr1, arr2):
        new_arr1 = set(arr1) # 1,2,3
        new_arr2 = set(arr2) # 2,3
        intersection = set()
        for i in new_arr1:
            if i in new_arr2:
                intersection.add(i)
        if intersection:
            return list(intersection)
        return None
    
    def IntersectionTwoArrays2(self, arr1, arr2):
        new_arr1 = set(arr1) # 1,2,3
        new_arr2 = set(arr2) # 2,3
        
        intersection = []
        
        for i in new_arr1:
            if i in new_arr2 :
                intersection.append(i)
        if intersection:
            return intersection
        return None
        
solution = Solution()

arr1 = [1, 2, 2, 1, 3]
arr2 = [2, 2, 3]
result = solution.IntersectionTwoArrays1(arr1, arr2)
print(result)  

arr3 = [4, 9, 5]
arr4 = [9, 4, 9, 8, 4]
result = solution.IntersectionTwoArrays2(arr3, arr4)
print(result)  


