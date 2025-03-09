class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        falsy = 0
        l,r = 0,1
        n = len(colors)
        while r<k:
            if colors[(r)%n]==colors[(r-1)%n]:
                falsy+=1
            r+=1
        print(falsy)
        count  = 0
        m = 2*n
        while l<n:
            if falsy==0:
                print(l,r)
                count+=1
            if colors[l]==colors[(l+1)%n]:
                falsy-=1
            if r<m and colors[(r)%n]==colors[(r-1)%n]:
                falsy+=1
            r+=1
            l+=1
        return count