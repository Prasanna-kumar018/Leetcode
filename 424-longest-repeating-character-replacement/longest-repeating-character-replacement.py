class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = -1
        n = len(s)
        left ,right = 0,n
        def isSafe(idx):
            if idx==0:
                return True
            d=collections.defaultdict(int)
            l,r=0,0
            while r<idx:
                d[s[r]]+=1
                r+=1
            while r<=n:
                val = max(d.values())
                # print("sdf",val)
                if val+k >=idx:
                    return True
                if r<n:
                    d[s[r]]=d.get(s[r],0)+1
                d[s[l]]=d.get(s[l],0)-1
                l+=1
                r+=1
            return False
        while left<=right:
            mid = (left+right)//2 
            if isSafe(mid):
                left=mid+1
                ans=mid
            else:
                right=mid-1
        return ans
        