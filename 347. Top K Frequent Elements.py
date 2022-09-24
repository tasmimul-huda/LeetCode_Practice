from typing import  List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List:
        count = {}
        freq = [[] for i in range(len(nums) +1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n,c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1, 0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) ==k:
                    return res
from collections import Counter
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List:
        n = len(nums)
        frequencies = [[] for _ in range((n+1))]

        for num, freq in Counter(nums).items():
            frequencies[freq].append(num)

        top_k = []
        while k:
            while not frequencies[n]:
                n -=1
            top_k.append(frequencies[n].pop())
            k -=1
        return top_k

a = Solution2()
nums = [2,1,1,2,2,3]
k = 2
print(a.topKFrequent(nums, k))
