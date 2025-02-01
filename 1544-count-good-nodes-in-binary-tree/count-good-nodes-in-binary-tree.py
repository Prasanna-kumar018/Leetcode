# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def recur(root,x):
            nonlocal ans
            if not root:
                return 
            if root.val>=x:
                ans+=1
            recur(root.left,max(x,root.val))
            recur(root.right,max(x,root.val))
        recur(root,root.val)
        return ans