class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        """
        Watch this for Range Update on fenwick Tree
        https://www.youtube.com/watch?v=gaAdpq1IyCI&t=25s

        x  1-based indexing     1    2    3    4    5
        increase                0    3    3    3    0  (d=3) 
        slope                        3    0    0   -3   
                                     3    3    3
        slope * x                   3*2  3*3  3*4 -3*5
        const                      -1*3   0    0   4*5  -(-3*5-1*5)
                                   -1*3  -1*3 -1*3  0
        """
        MOD = 10**9 + 7
        N = len(nums)
        res = 0
        tree1 = [0]*(N+1)
        tree2 = [0]*(N+1)
        def update(tree,idx,d):
            while idx<=N:
                tree[idx]+=d
                idx+=(idx&(-idx))
        def get(tree,idx):
            s = 0
            while idx>0:
                s += tree[idx]
                idx -= (idx&(-idx))
            return s
        def gett(idx): # idx is one based
            return get(tree1,idx)*idx + get(tree2,idx)
        def getit(l,r):
            return gett(r+1)-gett(l)
        def updateit(l,r,d): # d here is the increment value
            update(tree1,l+1,d)
            update(tree1,r+2,-d)
            # update(tree2,l+1,-((l+1)-1)*d)
            update(tree2,l+1,-l*d)
            update(tree2,r+2,(r+1)*d)
        """
        a2+b2+c2 = (a+1)2 + (b+1)2 + c2 = > a2 + b2+ c2 + 2a + 1 + 2b + 1
        a2 + b2+ c2 + 2*(a+b) + (1 + 1)
                      L * s   + L 
                      s is the sum of a and b
        """
        last = collections.defaultdict(lambda : -1)
        total = v = 0
        for idx,val in enumerate(nums):
            l,r = last[val]+1,idx
            s = getit(l,r) # 0 based inclusive
            # s is the sum from index [l->r] inclusive
            L = (r-l+1)
            v = (v + 2*s + L)
            total += v
            total %= MOD
            updateit(l,r,1) # 0 based inclusive
            last[val]=idx
        return total