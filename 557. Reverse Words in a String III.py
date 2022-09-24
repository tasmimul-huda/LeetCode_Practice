class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(list(map(lambda word:word[::-1], s.split())))

class Solution2:
    def reverseWords(self, s: str) -> str:
        return ' '.join([w[::-1] for w in s.split(" ")])
a = Solution2()
s = "Let's take LeetCode contest"
print(a.reverseWords(s))
