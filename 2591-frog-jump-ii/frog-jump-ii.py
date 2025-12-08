class Solution:
    def maxJump(self, stones: List[int]) -> int:
        n = len(stones)
        def isSafe(val):
            stone = stones[:]
            prev = 0
            i = 0
            while i<n-1:
                t = i
                while i+1<n and stone[i+1]-prev<=val:
                    i+=1
                if i==t:
                    return False
                prev = stone[i]
                if i!=n-1:
                    stone[i]=-1
            i = 0
            prev = 0
            while i<n-1:
                f = -1
                while i+1<n and (stone[i+1]==-1 or stone[i+1]-prev<=val):
                    if stone[i+1]!=-1:
                        f = i+1
                    i+=1
                if f==-1:
                    return False
                prev = stone[f]
            return True

        l,r,ans = 0,10**10,0
        while l<=r:
            mid = (l+r)//2
            if isSafe(mid):
                r = mid-1
                ans = mid
            else:
                l = mid+1
        return ans