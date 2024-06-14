class Solution:
    def countEventAndOld(self, arr):
        countEven = 0;
        countOld = 0;
        
        for i in range(len(arr)):
            if arr[i] % 2 == 0:
                countEven += 1;

            else:
                countOld +=1;
        return countEven, countOld;

#Khởi tạo đối tượng solution để gọi lớp Solution()
solution = Solution();
countEven, countOld = solution.countEventAndOld([1, 2, 3, 4, 5])
print(f"The number of even numbers is {countEven}, and the number of odd numbers is {countOld}.");