"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        
        def recur(x,y):
            node = Node()
            if x and x.isLeaf and y and y.isLeaf:
                node.isLeaf = True
                node.val = x.val or y.val
                return node
            if (x and x.isLeaf and x.val) or (y and y.isLeaf and y.val):
                node.isLeaf = True
                node.val = True
                return node
            if x and x.isLeaf and not y:
                node.isLeaf = True
                node.val= x.val
                return node
            if y and y.isLeaf and not x:
                node.isLeaf = True
                node.val= y.val
                return node
            node.topLeft= recur(x.topLeft if x else x,y.topLeft if y else y )
            node.topRight= recur(x.topRight if x else x,y.topRight if y else y)
            node.bottomLeft= recur(x.bottomLeft if x else x,y.bottomLeft if y else y)
            node.bottomRight= recur(x.bottomRight if x else x,y.bottomRight if y else y)
            if node.topLeft.isLeaf and node.topLeft.val and node.topRight.isLeaf and node.topRight.val and node.bottomLeft.isLeaf and node.bottomLeft.val and node.bottomRight.isLeaf and node.bottomRight.val:
                node.isLeaf = True
                node.topLeft= None
                node.topRight= None
                node.bottomLeft= None
                node.bottomRight= None
                node.val = True
            return node

        return recur(quadTree1,quadTree2)