class Solution:
    def coloredCells(self, n: int) -> int:
        """
        2 3 4 (square)
        0 1 2 

      1  4  9 16
      1  5   
        1 4 10
        1 4 13
        """

        n-=1
        ans = 1
        c = 2
        for i in range(n):
            ans += 2*c + 2*(c-2)
            c+=1
        return ans
