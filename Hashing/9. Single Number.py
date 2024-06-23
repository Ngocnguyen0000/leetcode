class Solution:
    def singleNumber(self, arr):
        count = {}
        for i in range(len(arr)):
            if arr[i] in count:
                count[arr[i]] += 1
            else:
                count[arr[i]] = 1
        for i in range(len(arr)):
            if count[arr[i]] == 1:
                return arr[i]
        return -1

# Ví dụ sử dụng
solution = Solution()
arr = [4,1,2,1,2]
print(solution.singleNumber(arr))