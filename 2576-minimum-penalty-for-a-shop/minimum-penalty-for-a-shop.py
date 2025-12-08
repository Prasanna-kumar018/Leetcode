class Solution:
    def bestClosingTime(self, customers: str) -> int:
        """
        N|Y
        """
        customers +='X' # Dummy
        Y = customers.count('Y')
        N = 0
        INF = 10**20
        ans = INF
        res = -1
        for idx,x in enumerate(customers):
            if ans > N+Y:
                ans = N+Y
                res = idx
            N += 1 if x=='N' else 0
            Y -= 1 if x=='Y' else 0
        return res