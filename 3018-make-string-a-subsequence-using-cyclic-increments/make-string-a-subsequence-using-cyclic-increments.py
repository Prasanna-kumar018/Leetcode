class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = 0
        M = len(str1)
        N = len(str2)
        for idx,val in enumerate(str1):
            x =  chr(((ord(str1[idx])-ord('a')+1)%26)+ord('a'))
            if i<N and (val==str2[i] or x==str2[i]):
                i+=1
        
        return i==N
        