from collections import defaultdict

class Solution:
    def groupAnagrams(self,strs: list[str]) -> list[list[str]]:
        sorted_words = defaultdict(list)
        
        for word in strs:
            letter_list = [c for c in word]
            letter_list.sort()
            sorted_word = "".join(letter_list)
            sorted_words[sorted_word].append(word)

        return list(sorted_words.values())
    
strs = ["eat","tea","tan","ate","nat","bat"]

a = Solution()

print(a.groupAnagrams(strs))
