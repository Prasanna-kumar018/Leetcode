class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # sort as they have +ve and -ve values 
        # first insert all the elements smaller than a particular element irrespective of idx
        # then count the number of indices that are greater than the particular element's idx...
        n=len(nums)
        tree = [0]*(n+1)
        l = [[v,idx+1] for idx, v in enumerate(nums)]
        l.sort(key=lambda x:x[0])
        res = [0]*n
        def get(idx):
            s=0
            while idx>0:
                s+=tree[idx]
                x=(idx&(-idx))
                idx-=x
            return s
        def update(idx):
            while idx<=n:
                tree[idx]+=1
                idx += (idx&(-idx))

        for v,idx in l:
            res[idx-1]=get(n)-get(idx)
            update(idx)
        return res
