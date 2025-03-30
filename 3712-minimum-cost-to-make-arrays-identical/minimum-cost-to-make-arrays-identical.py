class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        ini = 0
        for x,y in zip(arr,brr):
            ini += abs(x-y)

        arr.sort()
        brr.sort()
        res = 0
        for x,y in zip(arr,brr):
            res += abs(x-y)
        return min(ini,res+k)