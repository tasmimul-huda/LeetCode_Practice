from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)
        for num in nums:
            if (num-1) not in numSet:
                seq = 1
                while (num+seq) in numSet:
                    seq +=1
                longest = max(seq, longest)
        return longest



a = Solution()
nums = [100,4,200,1,3,2]
print(a.longestConsecutive(nums))
