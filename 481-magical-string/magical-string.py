class Solution:
    def magicalString(self, n: int) -> int:
        """
        1 2 2 1 1 2 1 2 2 1 2 2 1 1 2 1 1 2 2
        1 2 2 1 1 2 1 2 2 1 2 2
        """
        current_digit = 2
        q = collections.deque([2])
        total = 1
        for a in range(1,n):
            x = q.popleft()
            for _ in range(x):
                q.append(current_digit)
            if a == 1:
                q.popleft() 
            if x == 1:
                total+=1
            if current_digit == 1:
                current_digit = 2
            else:
                current_digit = 1
            # print(q)
        return total
