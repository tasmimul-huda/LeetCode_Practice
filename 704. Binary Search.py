from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left<=right:
            mid = (left + right)//2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                left = mid+1
            else:
                right = mid-1
        return -1

nums = [-1,0,3,5,9,12]
target = 9

a = Solution()
print(a.search(nums, target))
