class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        res = []
        for x in timePoints:
            arr = x.split(':')
            res.append((int(arr[0]),int(arr[1])))
        res.sort()
        ans = 10**20
        n = len(res)
        for i in range(1,n):
            a ,b = res[i-1]
            c , d = res[i]
            ans = min(ans,60*(c-a)+(d-b))
        a,b = res[0]
        c,d = res[-1]
        print(res)
        if len(res)>1:
            ans = min(ans,60*a+b+(23-c)*60+(60-d))
        return ans
