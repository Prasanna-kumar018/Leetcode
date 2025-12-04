# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        ans = collections.defaultdict(int)
        def recur(root):
            if not root:
                return 0

            l = recur(root.left)
            r = recur(root.right)
            v = l+r+root.val
            ans[v]+=1
            return v
        recur(root)
        MAXI = max(ans.values())
        res = []
        for x,y in ans.items():
            if y==MAXI:
                res.append(x)
        return res