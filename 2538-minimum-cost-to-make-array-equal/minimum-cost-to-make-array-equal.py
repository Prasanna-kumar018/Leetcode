class Solution:
    def minCost(self, nums: List[int], cc: List[int]) -> int:
        arr = [(x,y) for x,y in zip(nums,cc)]
        arr.sort(key=lambda x: x[0])
        n = len(nums)
        print(arr)
        prefixcv = [0]*n
        prefixcv[0]=arr[0][0]*arr[0][1]
        for i in range(1,n):
            prefixcv[i]=prefixcv[i-1]+(arr[i][0]*arr[i][1])
        
        prefixc = [0]*n
        prefixc[0]=arr[0][1]
        for i in range(1,n):
            prefixc[i]=prefixc[i-1]+(arr[i][1])

        suffixcv = [0]*n
        suffixcv[-1]=arr[-1][0]*arr[-1][1]
        for i in range(n-2,-1,-1):
            suffixcv[i]=suffixcv[i+1]+(arr[i][0]*arr[i][1])

        suffixc = [0]*n
        suffixc[-1]=arr[-1][1]
        for i in range(n-2,-1,-1):
            suffixc[i]=suffixc[i+1]+(arr[i][1])
        INF = 10**20
        res = INF
        for i in range(n):
            left = (arr[i][0]*(prefixc[i-1] if i-1>=0 else 0))-(prefixcv[i-1] if i-1>=0 else 0)
            right = (suffixcv[i+1] if i+1<n else 0)-(arr[i][0]*(suffixc[i+1] if i+1<n else 0))
            res = min(res,left+right)
        return res