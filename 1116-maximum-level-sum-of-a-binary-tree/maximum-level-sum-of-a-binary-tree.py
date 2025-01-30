# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        q.append(root)
        res = -1
        maxi = float('-inf')
        level = 1
        while q:
            s = sum([x.val for x in q])
            if s > maxi:
                maxi=s
                res = level
            size = len(q)
            while size>0:
                x = q.popleft()
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
                size-=1
            level+=1
        return res
