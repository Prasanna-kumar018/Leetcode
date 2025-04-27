class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        @cache
        def recur(left,right,k):
            if left>=right:
                return True
            res = False
            if s[left]==s[right]:
                res = res or recur(left+1,right-1,k)
            if k>0:
                res = res or recur(left+1,right,k-1)
                res = res or recur(left,right-1,k-1)
            return res
        return recur(0,n-1,1)