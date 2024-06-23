class Solution:
    def twoSum(self, nums, target):
        num_map = {} 
        for i in range(len(nums)):
            num = nums[i]  
            complement = target - num  
            if complement in num_map:  
                return [num_map[complement], i] 
            num_map[num] = i

nums = [2, 7, 11, 17]
target = 9

solution = Solution()
print(solution.twoSum(nums, target)) 
