class Solution:
    def TopFrequent(self, arr, k):
        count = {}
        for i in arr:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        frequent = []
        keys = list(count.keys())
        for i in range(len(keys)):
            if count[keys[i]] >= k:
                frequent.append(keys[i])
        
        return frequent

# Ví dụ
solution = Solution()
arr = [1,1,1,2,2,3]
k = 2
print(solution.TopFrequent(arr, k)) 