class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        count = 0
        while dividend > divisor:
            dividend -=divisor
            count +=1
        return count


dividend = 10
divisor = 3
a = Solution()

print(a.divide(dividend, divisor))
