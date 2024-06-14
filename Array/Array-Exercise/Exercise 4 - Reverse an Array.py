class Solution:
    def reverse(self, arr):
        
        left = 0
        right = len(arr) - 1
        while left < right:
            tmp = arr[left]
            arr[left] = arr[right]
            arr[right] = tmp
            left+=1
            right-=1
            
        return arr
    
solution = Solution();
print(solution.reverse([1, 2, 3, 4, 5,6,7,8,9]))

# [1, 2, 3, 4, 5,6,7,8,9]
# [9, 8, 7, 6, 5, 4, 3, 2, 1]


             
            
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#        i=l=0                   r  --> arr[0] = arr[8] --> [9, ...., 1]
#           i=l=1                   r  --> arr[1] = arr[7] --> [9, 8 ....,2, 1]
#              i=l=2                   r  --> arr[2] = arr[6] --> [9, 8,7 ....3,2, 1]
# ........................
 