class Solution:
    def deleteElement(self, arr, position):
        
        if position < 0 or position >= len(arr):
            return -1
        
        delete_arr = []
        for i in range(len(arr)):
            if i != position:
                delete_arr.append(arr[i])
        return delete_arr

solution = Solution()
arr = [1, 2, 3, 4, 5]
#      i = 0 --> i != position (0 != 1) --> delete_arr.append(arr[0]) --> [1]
#         i = 1 --> i = position (0 = 1) --> delete_arr --> [1]
#            i = 2 --> i != position (2 != 1) --> delete_arr.append(arr[2]) --> [1, 3]
#               i = 3 --> i != position (3 != 1) --> delete_arr.append(arr[3]) --> [1, 3, 4]
#                  i = 4 --> i != position (4 != 1) --> delete_arr.append(arr[4]) --> [1, 3, 4, 5]


position = 1                                 
delete_arr = solution.deleteElement(arr, position)

if position < 0 or position >= len(arr):
    print(-1)
else:   
    print(f"The array after deletion is {delete_arr}")