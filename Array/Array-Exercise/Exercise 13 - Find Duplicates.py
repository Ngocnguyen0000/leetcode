# class Solution:
#     def findremove(self, arr):
#         new_arr = set()
#         remove = set()
        
#         for i in range(len(arr)):
#             if arr[i] in new_arr:
#                 remove.add(arr[i])
#             else:
#                 new_arr.add(arr[i])
#         return list(remove)
    
    
    
#         # mp = {}
#         # for i in range(len(arr)):
#         #     if arr[i] in mp:
#         #         mp[arr[i]] += 1
#         #     else:
#         #         mp[arr[i]] = 0
#         # remove = []
#         # for key in mp:
#         #     if mp[key] > 0:
#         #         remove.append(key)
#         # return remove
        


# solution = Solution()
# arr = [4, 8, 9,1,3]
  
# result = solution.findremove(arr)
# print("The remove are", result)


class Solution:
    def findremove(self, arr):
        new_arr = set()
        remove = set()
        
        for i in range(len(arr)):
            if arr[i] in new_arr:
                remove.add(arr[i])
            else:
                new_arr.add(arr[i])
        return list(remove)

solution = Solution()
arr = [4, 8, 9, 1, 3, 4, 1, 9]
result = solution.findremove(arr)
print(result)

