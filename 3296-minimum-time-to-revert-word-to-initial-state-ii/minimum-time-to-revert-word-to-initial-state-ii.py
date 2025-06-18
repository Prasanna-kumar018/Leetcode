class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        count = 0
        hash = 0
        d = 26
        MOD = 10**12+7
        arr = []
        for x in word:
            x = ord(x)
            hash = (hash*d) + x
            hash %= MOD
            arr.append(hash)
        i = 0

        def get(x,y):
            a = y-x+1
            aa = pow(d,a,MOD)
            return ((arr[y]-((arr[x-1] if x-1>=0 else 0)*aa)%MOD)) % MOD
        while i+k<n:
            count += 1
            L = n-(i+k)
            start = get(0,L-1) 
            w = get(i+k,n-1)
            if start == w:
                return count
            i+=k
        count+=1
        return count