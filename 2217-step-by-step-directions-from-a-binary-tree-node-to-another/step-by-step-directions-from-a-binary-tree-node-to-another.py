# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        d = {}
        start = None
        def dfs(root,par):
            nonlocal start,d
            if not root:
                return 
            if root.val==startValue:
                start = root
            d[root]=par
            dfs(root.left,root)
            dfs(root.right,root)
        dfs(root,TreeNode(-1))
        # print(start,d)
        q = collections.deque()
        def traverse(root,par):
            nonlocal q
            if not root:
                return False
            # print(root.val)
            if root.val==destValue:
                return True
            if root.left!=par and traverse(root.left,root):
                q.appendleft('L')
                return True
            if root.right!=par and traverse(root.right,root):
                q.appendleft('R')
                return True
            if root in d and d[root]!=par and  traverse(d[root],root):
                q.appendleft('U')
                return True
            return False
        traverse(start,TreeNode(-2))
        return ''.join(list(q))