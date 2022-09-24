from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        l =0
        r = len(s) -1
        while l<r:
            s[r], s[l] = s[l], s[r]
            l +=1
            r -=1
        return s


class Solution2:
    def reverseString(self, s: List[str]) -> None:
        l =0
        r = len(s) -1
        while l<r:
            s[r], s[l] = s[l], s[r]
            l +=1
            r -=1
        return s

class Solution3:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        i = 0
        while i < n//2:
            s[i], s[n-i-1] = s[n-i-1], s[i]
            i = i+1



    
a = Solution3()
s = ["h","e","l","l","o","i", "p", "q"]

print(a.reverseString(s))
