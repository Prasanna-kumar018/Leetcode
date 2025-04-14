# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = set()
        def depth(root):
            if not root:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            return max(left,right)+1
        maxi = depth(root)
        def recur(root,dep):
            nonlocal maxi
            if not root:
                return
            if dep==maxi:
                q.add(root)
                return
            recur(root.left,dep+1)
            recur(root.right,dep+1)
        recur(root,1)
        def lca(root):
            if not root or root in q:
                return root
            left = lca(root.left)
            right = lca(root.right)
            if not left:
                return right
            if not right:
                return left
            return root
        return lca(root)