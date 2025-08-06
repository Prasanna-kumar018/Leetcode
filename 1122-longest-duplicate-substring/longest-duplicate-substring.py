class Solution:
    def longestDupSubstring(self, s: str) -> str:
        mod=1e12+7
        n=len(s)
        def isPossible(len_):
            l=0
            r=len_-1
            value = 0
            for i in range(l,r+1):
                asc= ord(s[i])
                value =  (value *26 + asc)%mod
            d={}
            d[value]=0
            while r+1 <n:
                r+=1
                asc= ord(s[l])
                # Use array to calculate power based on the mod value otherwise too long number will be created
                value = (((value-(power[len_-1]*asc)%mod)*26)%mod+ (ord(s[r])))%mod
                l+=1
                if value in d:
                    return d[value]
                else:
                    d[value]=l
            return -1
        power=[0]*n
        power[0]=1
        for i in range(1,n):
            power[i]=(power[i-1]*26)%mod
        l,r=1,n-1
        ans =""
        while l <= r:
            mid= (l+r)//2
            x=isPossible(mid)
            if  x!=-1:
                l = mid+1
                if len(ans) < len(s[x:(x+mid)]):
                    ans=s[x:(x+mid)]
            else:
                r=mid-1
        return ans