class Solution:
    def countBits(self, n: int) -> List[int]:
        ones = []
        for i in range(n+1):
            ans = sum(c=='1' for c in bin(i)[2:])
            ones.append(ans)
        return ones
            
        
