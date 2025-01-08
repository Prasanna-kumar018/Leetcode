class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key= lambda x:(x[0],-x[2]))
        n = len(events)
        q = []
        def get(start,val):
            l,r = start,n-1
            ans = n
            while l<=r:
                mid = (l+r)//2
                if events[mid][0]>=val:
                    ans = mid
                    r =mid-1
                else:
                    l = mid+1
            return ans
        @cache
        def recur(idx,k):
            if k==0:
                return 0
            if idx==n:
                return 0
            # skip
            best = recur(idx+1,k)
            # pick 
            next_one = get(idx+1,events[idx][1]+1)
            x =  recur(next_one,k-1)+events[idx][2]
            best = max(best,x)
            return best
        res = recur(0,k)
        return res