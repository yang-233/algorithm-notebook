from typing import *
import copy


class Solution:
    @staticmethod
    def binary_search(a, l, r, val):
        idx = -1
        while l <= r:
            mid = (l + r) // 2
            if a[mid] == val:
                idx = mid
                r = mid - 1
            elif a[mid] > val:
                r = mid - 1
            else:
                l = mid + 1
        return idx
    
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return None
        n = len(nums)
        temp = copy.deepcopy(nums)
        temp.sort()
        a = []
        for i in nums: # 离散化
            a.append(self.binary_search(temp, 0, n - 1, i) + 1)
        print(a)
        class Bit:
            @staticmethod
            def lowbit(x):
                return x & (-x)
            
            def __init__(self, n):
                self.n = n
                self.a = [0 for _ in range(n + 1)]

            def query(self, x):
                res = 0
                while x > 0:
                    res += self.a[x]
                    x -= self.lowbit(x)
                return res

            def update(self, x, val=1):
                while x <= self.n:
                    self.a[x] += val
                    x += self.lowbit(x)
                    
        bit = Bit(n)
        res = [0 for _ in range(n)]
        for i in range(n - 1, -1, -1):
            res[i] = bit.query(a[i] - 1)
            bit.update(a[i])
        return res

s = Solution()
nums = [5,2,6,1]
print(s.countSmaller(nums))