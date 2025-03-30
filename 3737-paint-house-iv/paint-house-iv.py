class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        INF = 10**20
        @cache
        def recur(left,right,idx):
            if idx==(n//2):
                if left==right:
                    return INF
                return 0 
            res = INF
            for c1 in range(3):
                for c2 in range(3):
                    if c1!=left and c2!=right and c1!=c2:
                        res = min(res,recur(c1,c2,idx+1)+cost[idx][c1]+cost[n-1-idx][c2])
            return res
        return recur(-1,-1,0)