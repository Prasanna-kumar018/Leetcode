class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        g = collections.defaultdict(list)
        
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)
        arr = [0]*n
        def go(node,par):
            total = values[node]
            for des in g[node]:
                if des!=par:
                    total += go(des,node)
            arr[node]=total
            return total
        go(0,-1)
        count = 0
        for x in arr:
            if x%k==0:
                count +=1
        return count