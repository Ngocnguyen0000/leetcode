class Solution:
    def copyArray(self, array1, array2):
        for element in array1:
            array2.append(element)
        return array2

solution = Solution()
array1 = [1, 2, 3, 4, 5]
array2 = []
copied_array = solution.copyArray(array1, array2)
print("The copied array is:", copied_array)
