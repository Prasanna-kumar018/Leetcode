class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        d = collections.defaultdict(list)
        for x,y in edges:
            d[x].append(y)
            d[y].append(x)
        s = sum(values)
        def dfs(start,par):
            m = 0
            for x in d[start]:
                if x !=par:
                    m+=dfs(x,start)
            return min(m if m!=0 else values[start],values[start])       
        return s-dfs(0,-1)
        