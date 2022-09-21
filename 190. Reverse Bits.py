class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            print((n >> i))
            res += (bit << (31 - i))
        #return res


n = 512
a = Solution()
print(a.reverseBits(n))
