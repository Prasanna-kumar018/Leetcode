class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        n = len(value)
        arr = [(x,y) for x,y in zip(value,limit)]
        arr.sort(key= lambda x:(x[1],-x[0]))
        maxi = 0
        total = 0
        left = 0
        for idx,(v,l) in enumerate(arr):
            if l<=maxi: # forward
                continue
            while left<=idx and arr[left][1]<=maxi:
                left+=1
            active = idx-left
            if active < l:
                total += v
                active += 1
            maxi = max(maxi,active)
        return total