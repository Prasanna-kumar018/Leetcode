class Solution:
    def maxPower(self, stations: List[int], ra: int, k: int) -> int:
        n = len(stations)
        prefix = [0]*n
        prefix[0]=stations[0]
        for i in range(1,n):
            prefix[i]= (prefix[i-1]+stations[i])
        # print(prefix)
        def get(x,y):
            return prefix[y]-(prefix[x-1] if x-1>=0 else 0)
        def isSafe(target):
            curr = 0
            added=0
            q = collections.deque()
            for i in range(n):
                while q and q[0][0]<i:
                    _,t = q.popleft()
                    curr-=t
                x = max(0,i-ra)
                y = min(i+ra,n-1)
                # print(x,y,get(x,y))
                now = get(x,y)+curr
                
                if now<target:
                    delta = target-now
                    added+=delta
                    curr+=delta
                    q.append((i+ra+ra,delta))
                # print(now,curr,added)
                if added>k:
                    return False
            return True
        l,r = 0,10**20
        while l<=r:
            mid = (l+r)//2
            if isSafe(mid):
                print(mid)
                l = mid+1
                ans = mid
            else:
                r = mid-1
        return ans
