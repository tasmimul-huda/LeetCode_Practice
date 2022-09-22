class Solution:
    def reverse(self, x: int) -> int:
        negative = x<0
        x = abs(x)
        reverse = 0
        while x !=0:
            reverse =reverse * 10 + x %10
            x //=10
        if reverse > 2**31 -1:
            return 0
        return reverse if not negative else -reverse


x = -123
a = Solution()

print(a.reverse(x))
