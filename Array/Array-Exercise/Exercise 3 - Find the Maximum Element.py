class Solution:
    def find_Mathximum(self, arr):
        m = arr[0]
        for i in range(1,len(arr)):
            if arr[i] > m:
                m = arr[i]
        return m

solution = Solution();

m = solution.find_Mathximum([1, 2, 3, 4, 5])
print(f"The maximum element is {m}")
