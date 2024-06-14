class Solution:
    def linearSearch(self, arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1

solution = Solution()
arr = [1, 2, 3, 4, 5]
target = 3
print(f'The element {target} is found at index {solution.linearSearch(arr, target)}')