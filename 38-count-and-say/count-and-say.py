class Solution:
    def countAndSay(self, n: int) -> str:
        def recur(n):
            if n==1:
                return '1'
            res = recur(n-1)
            ans = []
            for x,y in groupby(res):
                ans.append(str(len(list(y)))+x)
            return ''.join(ans)
        return recur(n)