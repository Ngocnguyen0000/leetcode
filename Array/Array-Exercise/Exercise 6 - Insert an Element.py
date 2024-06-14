class Solution:
    def insertElement(self, arr, position, value):
        
        if position < 0 or position > len(arr):
            return -1
        
        new_arr = []
        for i in range(len(arr)+1):
            if i < position:
                new_arr.append(arr[i])
            elif i == position:
                new_arr.append(value)
            else:
                new_arr.append(arr[i-1])
                
        return new_arr

solution = Solution()
arr = [1, 2, 3, 4, 5] 
# new_arr= []
#Run:  i=0 <position (0<2)--> new_arr.append(arr[0]) ==> new_arr = [1]
#         i=1 < positive (1<2)-->new_arr.append(arr[1]) ==> new_arr = [1, 2]
#           i=2 = position --> new_arr.append(value) ==> new_arr = [1,2,99]
#             i=3 >position --> new_arr.append(arr[2]) => new_arr = [1,2,99,3]
#               i=4 >position -->new_arr.append(arr[3]) => new_arr = [1,2,99,3,4]
#                   i=5 >position -->new_arr.append(arr[4]) => new_arr = [1,2,99,3,4,5]
position = 2
value = 99
new_arr = solution.insertElement(arr, position, value)

if position < 0 or position >= len(arr):
    print(-1)
else:
    print(f"The array after insertion is {new_arr}")

# O(n)