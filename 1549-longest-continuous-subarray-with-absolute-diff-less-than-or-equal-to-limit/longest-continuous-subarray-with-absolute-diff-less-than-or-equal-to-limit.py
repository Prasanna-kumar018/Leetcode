class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        x  = int(math.ceil(math.log2(n)))+1
        tree = [ 0 for _ in range(int(math.pow(2,x)))]
        def create(i,l,r):
            if l==r:
                tree[i]=(nums[l],nums[r])
                return 
            mid=(l+r)//2 
            create(2*i+1,l,mid)
            create(2*i+2,mid+1,r)
            tree[i] = ( min(tree[2*i+1][0],tree[2*i+2][0]), max(tree[2*i+1][1],tree[2*i+2][1]) )
        create(0,0,n-1)
        def get(i,l,r,x,y):
            if l>y or  r<x:
                return (float('inf'),float('-inf'))
            if l>=x and r<=y:
                return tree[i]
            mid = (l+r)//2
            a = get(2*i+1,l,mid,x,y) 
            b = get(2*i+2,mid+1,r,x,y)
            return (min(a[0],b[0]),max(a[1],b[1]))
        l , r =0,0
        res = 0
        while l<=r and r<n: 

            min_,max_ = get(0,0,n-1,l,r)
            if max_-min_ > limit:
                while l<r and  nums[l]!=min_ and nums[l]!=max_:
                    l+=1
                l+=1
            else:
                while r+1<n and min_ <= nums[r+1] <=max_:
                    r+=1
                res = max(res,r-l+1)
                r+=1
        return res
            