class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        l, r = 0,0
        z,o = 0,0
        n = len(s)
        arr = [0]*n
        while l<n and r<=n:
            while r<n and ((o +( 1 if s[r]=='1' else 0)) <=k or (z+( 1 if s[r]=='0' else 0))<=k):
                if s[r]=='0':
                    z+=1
                else:
                    o+=1
                r+=1
            arr[l]=r
            if s[l]=='0':
                z-=1
            else:
                o-=1
            l+=1
        prefix = [0]*n
        prefix[0]= arr[0]
        for i in range(1,n):
            prefix[i]=prefix[i-1]+(arr[i]-i)
        def get(x,y):
            return prefix[y]-(prefix[x-1] if x-1>=0 else 0)
        print(arr)
        def find(x,y):
            return (y*(y+1)//2) - ((x-1)*(x)//2)
        res = []
        for x,y in queries:
            l,r = x,y
            start  = -1
            while l<=r:
                mid = (l+r)//2
                if arr[mid]>=y+1:
                    start =mid
                    r = mid-1
                else:
                    l = mid+1
            value = 0
            if start-1>=x:
                value += get(x,start-1)
            length = y-start+1
            # print(value,start)
            if start!=-1:
                value += (length*(length+1))//2
            res.append(value)
        return res