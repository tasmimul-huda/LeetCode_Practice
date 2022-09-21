class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {'(':')', '{':'}','[':']'}

        for c in s:
            if c in match: ### check keys of dictionary
                stack.append(c)
            else:
                if not stack or (match[stack.pop()] !=c):
                    return False
        return not stack



s = "()[]{}"
a = Solution()
print(a.isValid(s))
