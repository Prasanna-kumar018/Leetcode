class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        s = sum(nums)
        half = s//2
        n = len(nums)
        N = n//2
        left = nums[:N]
        right = nums[N:]
        l,r = collections.defaultdict(list) , collections.defaultdict(list) 
        def recur(idx,c,arr,ll,val,end):
            if idx==end:
                ll[c].append(val)
                return 
            recur(idx+1,c,arr,ll,val,end)
            recur(idx+1,c+1,arr,ll,val+arr[idx],end)
        recur(0,0,left,l,0,len(left))
        recur(0,0,right,r,0,len(right))
        for x,y in r.items():
            y.sort()
        INF = 10**20
        res = INF
        for c,valv in l.items():
            for val in valv:
                nn = N-c
                need = half -val
                M = len(r[nn])
                ind1 = bisect.bisect_left(r[nn],need) # >= 
                ind2 = bisect.bisect_right(r[nn],need)-1 # <=
                # print(c,valv,val,ind1,ind2,need,r[nn])
                if 0<= ind1 <M:
                    # total- (sum-total)
                    # 2* total - sum or sum - 2*total
                    total = val + r[nn][ind1]
                    res = min(res,abs(s - (2*total)))
                if 0<= ind2 <M:
                    total = val + r[nn][ind2]
                    res = min(res,abs(s- (2*total)))
        return res
