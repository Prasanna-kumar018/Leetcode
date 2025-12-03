# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        path = []
        MAXI = 8501
        ans = ['z']*(MAXI)
        def recur(node):
            nonlocal ans
            if not node:
                return
            path.append(chr(node.val+97))
            if not node.left and not node.right:
                a = path[::-1]
                ans = min(a,ans)
                path.pop()
                return
            recur(node.left)
            recur(node.right)

            path.pop()
        recur(root)
        return ''.join(ans)