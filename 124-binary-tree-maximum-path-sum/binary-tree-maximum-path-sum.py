# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        INF = -10**20
        res = INF   
        def find(root): 
            nonlocal res
            if not root:
                return 0
            y = find(root.left)
            x = find(root.right)
            x = max(0,x)
            y = max(0,y)
            res = max(x+y+root.val,res)
            return max(x,y)+root.val
        find(root)
        return res