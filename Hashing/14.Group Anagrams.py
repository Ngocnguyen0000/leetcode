class Solution:
    def groupAnagrams(self, strs):
        anagram_groups = {}
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            
            if sorted_word in anagram_groups:
                anagram_groups[sorted_word].append(word)
            else:
                anagram_groups[sorted_word] = [word]
        
        result = list(anagram_groups.values())
        
        return result

solution = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
grouped_anagrams = solution.groupAnagrams(strs)

for group in grouped_anagrams:
    print(group)
