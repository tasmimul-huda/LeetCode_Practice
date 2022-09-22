from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        while left<= right:
            mid = (left+right) //2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                left = mid +1
            elif target < nums[mid]:
                right = mid -1
        return left

nums = [1,3,5,6]
target = 2

a = Solution()
print(a.searchInsert(nums, target))
