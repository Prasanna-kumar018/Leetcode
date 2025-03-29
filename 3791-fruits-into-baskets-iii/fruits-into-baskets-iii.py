class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n  = len(fruits)
        x = 4*n
        tree = [0]*x
        def create(i,l,r):
            if l==r:
                tree[i]=baskets[l]
                return
            mid = (l+r)//2
            create(2*i+1,l,mid)
            create(2*i+2,mid+1,r)
            tree[i]=max(tree[2*i+1],tree[2*i+2])
        create(0,0,n-1)
        def get(i,l,r,x):
            if tree[i]<x:
                return -1
            if l==r:
                return l
            mid = (l+r)//2
            if tree[2*i+1]>=x: # preference to left sub tree
                return get(2*i+1,l,mid,x)
            else:
                return get(2*i+2,mid+1,r,x)
        def update(i,l,r,index):
            if l==r:
                tree[i]=0
                return
            mid = (l+r)//2
            if index<=mid:
                update(2*i+1,l,mid,index)
            else:
                update(2*i+2,mid+1,r,index)
            tree[i]=max(tree[2*i+1],tree[2*i+2])
            
        count = 0
        for x in fruits:
            r = get(0,0,n-1,x)
            if r==-1:
                count+=1
                continue
            update(0,0,n-1,r)
        return count