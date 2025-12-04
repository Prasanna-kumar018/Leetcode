class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        m = len(word1)
        n = len(word2)
        a,b = Counter(word1),Counter(word2)
        M = 26
        for i in range(M):
            for j in range(M):
                x,y = chr(i+97),chr(j+97)
                if x in a and y in b:
                    a[x]-=1
                    b[y]-=1
                    if a[x]==0:
                        del a[x]
                    if b[y]==0:
                        del b[y]
                    a[y]+=1
                    b[x]+=1
                    if len(a)==len(b):
                        return True
                    a[y]-=1
                    b[x]-=1
                    if a[y]==0:
                        del a[y]
                    if b[x]==0:
                        del b[x]
                    a[x]+=1
                    b[y]+=1
        return False