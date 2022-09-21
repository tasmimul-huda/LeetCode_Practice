class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = 0
        while n>0:
            if n%2==1:
                print(f"n%2: {n%2}")
                ones+=1
                n-=1
                print(f"n-=1: {n}")
            n/=2
            print(f"n/=2 :{n}")
        return ones
class Solution2:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n%2
            print(f"n%2: {n%2}")
            print(f"n: {n}")
            n = n>>1
            print(f"n>>1: {n}")
        return res

class Solution3:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n = n & (n-1)
            print(f"n: {n}=== n-1 : {n-1}")
            res +=1
        return res

class Solution4:
    def hammingWeight(self, n: int) -> int:
        return sum(c =='1' for c in bin(n) [2:])

n = 15
print(bin(n))
a = Solution3()
print(a.hammingWeight(n))
