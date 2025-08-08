class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        INF = 10**20
        res = 0
        @cache
        def recur(l,r):
            if l==r:
                return (arr[l],0) # maxi, sum
            res = 0
            s = INF
            for i in range(l,r):
                left = recur(l,i) 
                right = recur(i+1,r)
                node = (left[0]*right[0])
                ss = node + left[1] + right[1]
                if ss < s:
                    s = ss
                    res = max(left[0],right[0])
                    
            return (res,s)
        x = recur(0,n-1)[1]
        return x