class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        k = k-1
        res = [x for x in range(1,n+1)]
        x = k%n
        while len(res)>1:
            res.pop(x)
            x = (x+k)%len(res)
        return res[0]