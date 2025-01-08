class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        N = len(nums)
        x = int(math.ceil(math.log2(N+1)))
        n = int(math.pow(2,x+1))
        tree = [[ [0]*2 for _ in range(2) ]  for _ in range(n)]
        def merge(l,r):
            ans = [ [0]*2 for _ in range(2) ]
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        ans[i][j] = max(ans[i][j],l[i][k]+r[1-k][j])
            return ans
        def create(i,l,r):
            if l==r:
                tree[i][1][1]=nums[r]
                return
            mid = (l+r)//2
            create(2*i+1,l,mid)
            create(2*i+2,mid+1,r)
            tree[i]= merge(tree[2*i+1],tree[2*i+2])
        create(0,0,N-1)
        def update(i,l,r,idx,val):
            if l==r:
                tree[i][1][1]=val
                return 
            mid = (l+r)//2
            if idx<=mid:
                update(2*i+1,l,mid,idx,val)
            else:
                update(2*i+2,mid+1,r,idx,val)
            tree[i]= merge(tree[2*i+1],tree[2*i+2])
        def get(i,l,r,x,y):
            if l>y or r<x:
                return [ [0]*2 for _ in range(2) ]
            if l>=x and r<=y:
                return tree[i]
            mid = (l+r)//2
            a = get(2*i+1,l,mid,x,y)
            b = get(2*i+2,mid+1,r,x,y)
            return merge(a,b)
        ans = 0 
        mod = 10**9 + 7
        for x,y in queries:
            update(0,0,N-1,x,y)
            val = get(0,0,N-1,0,N-1)
            maxi = max([max(x) for x in val])
            ans += maxi
        return ans%mod