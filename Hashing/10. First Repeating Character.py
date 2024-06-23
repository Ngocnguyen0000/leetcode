class Solution:
    def firstRepeat(self, s):
        count = {}
        for i in range(len(s)):
            if s[i] in count:
                count[s[i]] += 1
            else:
                count[s[i]] = 1
        for i in range(len(s)):
            if count[s[i]] == 1:
                return count[s[0]]
        return -1

solution = Solution()
s = "swiss"
print(solution.firstRepeat(s))
