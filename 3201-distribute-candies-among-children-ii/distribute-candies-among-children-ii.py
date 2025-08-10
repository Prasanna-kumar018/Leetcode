class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        """
        
        candies = 10
        limit = 6

        for remaining two
        j   k
        0   10
        1   9
        2   8
        3   7

        k is bigger than limit
    -----------
(candies-limit)
        4   6
        5   5
(limit) 6   4
----------------
        7   3
        8   2
        9   1
        10  0
        """
        total =0 
        for c in range(min(n,limit)+1):
            # c is the no of candies that child-1 takes
            candies = n -c
            if candies<=limit:
                total += candies + 1 # 1 for 0 count
            else:
                total += max(0,(limit-(candies-limit))+1)
                # +1 is for inclusive
        return total