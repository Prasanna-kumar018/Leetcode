class Solution:
    def nextGreaterElement(self, na: int) -> int:
        x = list(str(na))
        n = len(x)
        i = n-2
        while i>=0 and x[i]>=x[i+1]:
            i-=1
        if i>=0:
            j = n-1
            while j>i and x[j]<=x[i]:
                j-=1
            x[i],x[j]=x[j],x[i]

        def reverse(l,r):
            while l<r:
                x[l],x[r]=x[r],x[l]
                l+=1
                r-=1


        reverse(i+1,n-1)
        res= int(''.join(x))
        MAX = (1<<31)-1
        return res if res>na and res <=MAX else -1