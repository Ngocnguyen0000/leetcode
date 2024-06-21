class Solution:
    def move_zeroes(self, nums):
        index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                tpm = nums[index]
                nums[index] = nums[i] 
                nums[i] = tpm
                index += 1
        return nums

solution = Solution()
nums = [0, 1, 0, 3, 12]
result = solution.move_zeroes(nums)
print(result)
