class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indegree = [0]*n
        for x,y in zip(leftChild,rightChild):
            if x!=-1:
                indegree[x]+=1
            if y!=-1:
                indegree[y]+=1
        # print(indegree)
        root = -1
        for idx,val in enumerate(indegree):
            if val==0:
                root = idx
        # print(root)
        seen = [False]*n
        ans = True
        def recur(root):
            nonlocal ans
            if root==-1 or seen[root]:
                if root!=-1:
                    ans = False
                return 
            seen[root]=True
            recur(leftChild[root])
            recur(rightChild[root])
        recur(root)
        return seen==[True]*n and ans

        """
             0
            1 2
             3
        """