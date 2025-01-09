class Solution:
    def waysToReachStair(self, k: int) -> int:
        @cache
        def recur(start,used,j):
            if used and start>k:
                return 0
            if not used and start-1>k:
                return 0
            total = 0
            if start==k:
                total+=1
            
            if not used and start>0:
                total+= recur(start-1,True,j)
            total += recur(start+(1<<j),False,j+1)
            return total
        return recur(1,False,0)