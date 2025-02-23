# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        d = {}
        n = len(preorder)
        for idx,val in enumerate(postorder):
            d[val]=idx
        def recur(prestart,preend,poststart,postend):
            # print(prestart,preend,poststart,postend)
            if prestart>preend:
                return None
            if prestart==preend:
                return TreeNode(preorder[prestart])
            maxi = d[preorder[prestart+1]]
            i = prestart+1
            while maxi>i:
                maxi = max(maxi,d[preorder[i]])
                i+=1
            lsize = maxi-poststart+1
            rsize = postend-maxi-1
            node = TreeNode(preorder[prestart])
            node.left = recur(prestart+1,prestart+lsize,poststart,maxi)
            node.right = recur(preend-rsize+1,preend,maxi+1, postend-1)
            return node
        return recur(0,n-1,0,n-1)