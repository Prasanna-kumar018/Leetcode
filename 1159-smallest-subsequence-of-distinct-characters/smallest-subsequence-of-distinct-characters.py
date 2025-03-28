class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        vis = set()
        f = collections.Counter(s)
        for x in s:
            while stack and stack[-1]>x and (x not in vis) and f[stack[-1]]>0:
                a = stack.pop()
                vis.discard(a)
            f[x]-=1
            if x not in vis:
                vis.add(x)
                stack.append(x)
            # print(stack)
        return ''.join(stack)