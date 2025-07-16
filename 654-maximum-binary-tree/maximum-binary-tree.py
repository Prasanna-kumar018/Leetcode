# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        tree = [0]*(4*n)
        def create(i,l,r):
            if l==r:
                tree[i]= l
                return 
            mid = (l+r)//2
            create(2*i+1,l,mid)
            create(2*i+2,mid+1,r)
            tree[i]=tree[2*i+1] if nums[tree[2*i+1]]>=nums[tree[2*i+2]] else tree[2*i+2]
        create(0,0,n-1)
        def get(i,l,r,x,y):
            if l>=x and r<=y:
                return tree[i]
            if l>y or r<x:
                return -1
            mid = (l+r)//2
            left = get(2*i+1,l,mid,x,y)
            right = get(2*i+2,mid+1,r,x,y)
            if left == -1:
                return right
            if right == -1:
                return left
            return left if nums[left]>=nums[right] else right
        
        def recur(ll,rr):
            if ll>rr:
                return None
            index = get(0,0,n-1,ll,rr)
            node = TreeNode(nums[index])
            node.left = recur(ll,index-1)
            node.right = recur(index+1,rr)
            return node

        return recur(0,n-1)