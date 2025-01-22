class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = [int(c) for c in str(n)]
        x =len(s)
        t = []
        max_ = float('-inf')
        for  idx in range(x-1,-1,-1):
            i = s[idx]
            if i < max_:
                w = bisect.bisect_right(t,i)
                a = t[w] 
                s[idx] = a
                t.pop(w)
                t.append(i)
                break
            max_  = max(max_,i)
            t.append(i)
        t.sort(reverse = True)
        idx = len(s)-1
        i = 0
        while i<len(t):
            s[idx]=t[i]
            idx-=1
            i+=1 
        res = int(''.join(map(str,s)))
        print(res)
        return  res if len(t)!=x and res<=pow(2,31)-1 else -1