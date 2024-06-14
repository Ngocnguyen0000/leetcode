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
    
    
    
        # mp = {}
        # for i in range(len(arr)):
        #     if arr[i] in mp:
        #         mp[arr[i]] += 1
        #     else:
        #         mp[arr[i]] = 0
        # remove = []
        # for key in mp:
        #     if mp[key] > 0:
        #         remove.append(key)
        # return remove
        
class Solution:
    def findremove1(self, arr):
        new_arr1 = set()        
        remove1 = set()
        max_ = max(arr)
        
        for i in range(len(arr)):
            if arr[i] == max_ :
                remove1.add(arr[i])
            else:
                new_arr.add(arr[i])
        return list(new_arr1)
    
    def findremove2(self, arr):
        new_arr2 = set()        
        remove2 = set()
        max_ = max(arr)
        
        for i in range(len(arr)):
            if arr[i] == max_ :
                remove2.add(arr[i])
            else:
                new_arr.add(arr[i])
        return list(new_arr2)
    
    def findremove3(self, arr):
        new_arr3 = set()        
        remove3 = set()
        max_ = max(arr)
        
        for i in range(len(arr)):
            if arr[i] == max_ :
                remove3.add(arr[i])
            else:
                new_arr.add(arr[i])
        return list(new_arr3)
    
    def tong(self, arr):
        s = 0
        s = sum(new_arr2) + sum(new_arr3)
        return s
    

    
    
    
    

        
        

solution = Solution()
arr = [4, 8, 9,1,3]
  
result = solution.tong(arr)
print("The remove are", result)

