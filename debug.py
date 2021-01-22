from typing import *
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(root):
            if root is None:
                return None, None

            lmin, lmax = dfs(root.left)
            rmin, rmax = dfs(root.right)

            l = r = root
            root.left = root.right = None

            if lmax is not None: # 接上左侧最大的
                root.left = lmax
            if lmin is not None: # 左侧最小不是自身
                l = lmin

            if rmin is not None: # 接上右侧最小
                root.right = rmin
            if rmax is not None: # 如果右侧最大不是本身
                r = rmax
            print(root.val, l.val, r.val)
            return l, r
        
        lmin, rmax = dfs(root)
        lmin.left = rmax
        rmax.right = lmin
        return lmin
s = Solution()
l = s.