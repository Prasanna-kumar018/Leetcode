class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        """
        x is odd and y is even, or
        y is odd and x is even.
        """
        return m // 2 * (n // 2 + n % 2) + n // 2 * (m // 2 + m % 2)