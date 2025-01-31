# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        maxi = float('-inf')
        def recur(root):
            nonlocal maxi
            if not root:
                return (float('-inf'),0) # val,count
            left = recur(root.left)
            right = recur(root.right)
            a = b = 0
            if left[0]==root.val:
                a=left[1]
            if right[0]==root.val:
                b=right[1]
            maxi = max(maxi,1+a+b)
            return (root.val,1+max(a,b))
        x = recur(root)
        return maxi-1 if maxi!=float("-inf") else 0
