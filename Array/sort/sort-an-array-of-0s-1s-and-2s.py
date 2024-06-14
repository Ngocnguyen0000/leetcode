class Solution:
    def sort012(self, arr, n):
        def swap(arr, i, j):
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            # arr[i], arr[j] = arr[j], arr[i]
        left = 0
        right = n - 1
        index = 0

        while index <= right:
            if arr[index] == 0:
                swap(arr, left, index)
                left += 1
                index += 1
            elif arr[index] == 1:
                index += 1
            else:
                swap(arr, right, index)
                right -= 1

arr = [0, 2, 1, 2, 0]
n = len(arr)
solution = Solution()
solution.sort012(arr, n)
print(arr)

# Khi arr[index] là 0, hoán đổi nó với phần tử tại vị trí left và tăng cả left và index.
# Khi arr[index] là 1, chỉ tăng index.
# Khi arr[index] là 2, hoán đổi nó với phần tử tại vị trí right và giảm right.
