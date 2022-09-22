from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lst = [num*num for num in nums]
        lst.sort()
        return lst

class Solution2:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(map(lambda x:x*x,nums))

nums = [-4,-1,0,3,10]

a = Solution()
print(a.sortedSquares(nums))
