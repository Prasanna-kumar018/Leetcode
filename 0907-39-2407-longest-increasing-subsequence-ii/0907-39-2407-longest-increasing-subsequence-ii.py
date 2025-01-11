class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        n = max(nums)+1
        x = int(math.ceil(math.log2(n+1)))
        tree = [0]*(int(math.pow(2,x+1)))

        def update(i,l,r,idx,val):
            if l==r:
                tree[i]=max(tree[i],val)
                return
            mid = (l+r)//2
            if idx<=mid:
                update(2*i+1,l,mid,idx,val)
            else:
                update(2*i+2,mid+1,r,idx,val)
            tree[i]=max(tree[2*i+1],tree[2*i+2])
        def get(i,l,r,x,y):
            if l>y or r<x:
                return 0
            if l>=x and r<=y:
                return tree[i]
            mid = (l+r)//2
            a = get(2*i+1,l,mid,x,y)
            b = get(2*i+2,mid+1,r,x,y)
            return max(a,b)
        ans = 0
        for idx in range(len(nums)-1,-1,-1):
            val = nums[idx]
            a = get(0,0,n-1,min(val+1,n),min(val+k,n))
            # print(a,val,idx,tree)
            update(0,0,n-1,val,a+1)
            ans = max(ans,a+1)
        return ans
            