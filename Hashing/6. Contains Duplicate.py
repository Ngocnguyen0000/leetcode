# arr1 = [0, 2, 3, 0]
#                  i

class Solution:
    def constantDuplicate_solution1(self, arr):
        count = {} # {0:2 ; 2:1; 3:1;   }
        for i in range(len(arr)):
            if arr[i] in count:
                count[arr[i]] += 1
            else:
                count[arr[i]] = 1
            
            if count[arr[i]] > 1:
                return True
        return False
    
    def constantDuplicate_solution2(self, arr):
        arr.sort()  
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]: 
                return True
        return False

solution = Solution()
# Solution1 
# Time complexity: O(n)
# Space complexity: O(n)
arr1 = [0, 2, 3, 0]
result1 = solution.constantDuplicate_solution1(arr1)

print(result1) 
# Solution 2
# Time complexity: O(nlogn)
# Space complexity: O(n)
arr2 = [1, 2, 3, 1]
result2 = solution.constantDuplicate_solution2(arr2)
print(result2) 