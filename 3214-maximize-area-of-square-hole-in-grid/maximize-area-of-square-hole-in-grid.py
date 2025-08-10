class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hori = 0
        vert = 0
        i = 0
        hBars.sort()
        vBars.sort()
        M = len(hBars)
        N = len(vBars)
        while i<M:
            start = i
            while i+1<M and hBars[i+1]-hBars[i]==1:
                i+=1
            L = i-start+2
            hori = max(L,hori)
            i+=1 
        i = 0  
        while i<N:
            start = i
            while i+1<N and vBars[i+1]-vBars[i]==1:
                i+=1
            L = i-start+2
            vert = max(L,vert)
            i+=1   
        x = min(hori,vert)
        return x*x