class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        start = 0
        longest = 0

        for i, char in enumerate(s):
            if char in last_seen and last_seen[char]>= start:
                start = last_seen[char] + 1
            else:
                longest = max(longest,i-start+1)

            last_seen[char] = i
        return longest
        
a = Solution()
s = "abcabcbb"
print(a.lengthOfLongestSubstring(s))
