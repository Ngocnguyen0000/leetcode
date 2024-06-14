# array = [1, 2, 3, 4, 5]
# result = sum(array)
# print("The sum is" , result)


class Solution:
    def countSum(self, nums):
        s = 0;
        for i in range(len(nums)):
            s += nums[i]    
        return s
    
solutiton = Solution();
solutiton.countSum([1, 2, 3, 4, 5])
print(solutiton.countSum([1, 2, 3, 4, 5]))



