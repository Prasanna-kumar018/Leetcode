class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        m = len(queries)
        if nums.count(0)==n:
            return 0
        l,r = 0,m-1
        res = -1
        while l<=r:
            mid = (l+r)//2
            ans = True
            d = collections.defaultdict(list)
            for x,y,val in queries[:mid+1]:
                for idx in range(x,y+1):
                    d[idx].append(val)
            # print(mid,d)
            for i in range(n):
                a = len(d[i])
                @cache
                def go(idx,val):
                    if val<0:
                        return False
                    if idx==a:
                        if val==0:
                            return True
                        return False
                    t = False
                    t = t or go(idx+1,val)
                    t = t or go(idx+1,val-d[i][idx])
                    return t
                if not go(0,nums[i]):
                    ans = False
                    break
                go.cache_clear()
            if ans:
                r = mid-1
                res = mid+1
            else:
                l = mid+1
        return res