class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def recur(close,open,s):
            if close==0:
                if open==0:
                    res.append(s)
                return 
            recur(close-1,open+1,s+'(')
            if open>0:
                recur(close-1,open-1,s+')') 
        recur(2*n,0,'')
        return res