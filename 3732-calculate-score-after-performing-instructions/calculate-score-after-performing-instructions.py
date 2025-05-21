class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        n = len(values)
        vis = set()
        def recur(idx):
            if idx in vis or idx<0 or idx>=n:
                return 0
            vis.add(idx)
            ans = 0
            if instructions[idx]=='jump':
                ans += recur(idx+values[idx])
            if instructions[idx]=='add':
                ans += recur(idx+1)+values[idx]
            return ans
        return recur(0)