class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        i=0
        n = len(arr)
        res=0
        while i<n:
            maxi = arr[i]
            t = i
            while t<=maxi:
                maxi=max(maxi,arr[t])
                t+=1
            i=t
            res+=1
        return res