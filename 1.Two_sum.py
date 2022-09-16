class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        num_index_map = {} #num->key; index->value

        for i, num in enumerate(nums):

            if (target - num) in num_index_map:
                return [num_index_map[target-num], i]

            num_index_map[num] = i
        return []

nums = [2,7,11,15]
target = 9
a = Solution()

ret = a.two_sum(nums,target)
