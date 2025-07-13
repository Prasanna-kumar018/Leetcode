# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        q = []
        l = []
        while q or root:
            while root:
                q.append(root)
                root = root.left
            curr = q.pop()
            l.append(curr.val)
            root = curr.right
        return l