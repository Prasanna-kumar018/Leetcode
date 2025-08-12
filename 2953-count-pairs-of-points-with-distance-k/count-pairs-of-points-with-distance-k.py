class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        n = len(coordinates)
        """

    (x1 xor x2 )+( y1 xor y2 )
        0              k
        1             k-1
        2             k-2


        k              0
        """

        total = 0
        for kk in range(k+1):
            l,r = kk,k-kk
            seen = collections.defaultdict(int)
            for x,y in coordinates:
                total += seen[(l^x,r^y)]
                seen[(x,y)]+=1
        return total