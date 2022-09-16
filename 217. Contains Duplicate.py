class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:   
        return len(set(nums)) != len(nums)
nums = [1,2,3,1]
a = Solution()
print(a.containsDuplicate(nums))


"""
Explanation:
In pyhton, set doesn't contain any duplicate value...if there is any duplicate item in list
than set automatically remove the duplicate
"""
