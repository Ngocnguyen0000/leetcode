class Solution:
    def printArray(self, arr):
        for i in range(len(arr)):
            arr[i] = 0
        return arr

solution = Solution()
result = solution.printArray([1, 2, 3, 4, 5])
print(f"Modified array: {result}")
