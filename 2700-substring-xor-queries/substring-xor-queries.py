class Solution:
    def substringXorQueries(self, ss: str, queries: List[List[int]]) -> List[List[int]]:
        """

        2^1 + 2^2 + 2^3 .... + 2^30 

        atmost there are 32 bits 
        for len = 1
        n 
        for len = 2
        n -1 
        for len = 3
        n- 2
        for len = 32
        n - 31

        so ... 32*n - (1+....+32)  => so atmost 32*n 

        """
        n = len(ss)
        lookup = {}
        for L in range(1,33):
            mask = (1<<L)-1
            curr = 0
            for i in range(n):
                curr <<=1
                curr += int(ss[i])
                curr &= mask
                if i>=L-1 and curr not in lookup:
                    lookup[curr]=[i-L+1,i]
        res  = []
        for f,s in queries:
            val = s^f
            if val in lookup:
                res.append(lookup[val])
            else:
                res.append([-1,-1])
        return res