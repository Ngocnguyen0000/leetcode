class Solution:
    def SumTarget(self, nums, target):
        arr = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in arr:
                return [arr[complement], index]
            arr[num] = index

        return []

# nums = [2, 7, 11, 15]
# target = 9

# nums = [2, 9, 11, 15]
# target = 9

# nums = [2, 0, 7, 2]
# target = 9

nums = []
target = 9



solution = Solution()
result = solution.SumTarget(nums, target)
print(result) 


# Tu dien