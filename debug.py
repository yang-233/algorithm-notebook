from typing import *

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return None
        n = len(nums)
        for i in range(n):
            while nums[i] != i:
                if nums[nums[i]] == nums[i]:
                    return nums[i]
                nums[i], nums[nums[i]] = nums[nums[i]], nums[i] # 交换位置 这个写法有bug
                
#                 t1 = nums[i]
#                 nums[i] = nums[t1]
#                 nums[t1] = t1

s = Solution()
x = [2, 3, 1]
print(s.findRepeatNumber(x))