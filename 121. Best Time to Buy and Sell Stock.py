class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        buy = float('-inf')
        sell = 0
        
        for price in prices:
            buy = max(-price, buy)
            print(f"buy: {-buy}")
            sell = max(price+buy, sell)
            print(f"sell: {sell}")
        return sell

prices = [7,1,5,3,6,4]
a = Solution()

print(a.maxProfit(prices))
