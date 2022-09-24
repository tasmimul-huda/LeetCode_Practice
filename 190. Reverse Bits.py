class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n>>i)& 1
            res =res | (bit<< (31-i))
        return res
                    
class Solution2:
    def reverseBits(self, n: int) -> int:
        reverse, bit = 0, 31
        print("bin(n):",bin(n)[2:])
        i=0
        while i<32:
            if n % 2 ==1:
                reverse += 2**1
                print('reverse:', reverse)
                print('bin reverse:', bin(reverse)[2:])
                bit -=1
                print('bit:', bit)
                n //=2
                print('n: ',n)
                print('\\bin n: ',bin(n)[2:])
            i +=1
        return reverse
                
    

n = 11 #43261596
a = Solution2()
print(a.reverseBits(n))
