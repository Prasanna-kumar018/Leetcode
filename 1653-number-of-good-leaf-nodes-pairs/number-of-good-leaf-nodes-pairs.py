# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        par = {}
        leafs= []
        def traverse(root,parent):
            if not root:
                return 
            traverse(root.left,root)
            traverse(root.right,root)
            if not root.left and not root.right:
                leafs.append(root)
            par[root]=parent
        traverse(root,None)
        res = set()
        for l in leafs:
            t = distance+1
            q = collections.deque([(l,None,l)])
            while t>0 and q:
                size = len(q)
                while size>0:
                    x,parent,src = q.popleft()
                    if (not x.right) and (not x.left) and ((src,x) not in res) and ((x,src) not in res )and x!=src:
                        res.add((src,x))
                    if x.right and x.right!=parent:
                        q.append((x.right,x,src))
                    if x.left and x.left!=parent:
                        q.append((x.left,x,src))
                    if x in par and par[x] and par[x]!=parent:
                        q.append((par[x],x,src))
                    size-=1
                # print(q)
                # print()
                # print(res,t)
                t-=1
        # print()
        # print(res)
        return len(res)