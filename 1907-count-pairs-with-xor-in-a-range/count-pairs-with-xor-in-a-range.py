class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        class Node:
            def __init__(self):
                self.children=[None]*2
                self.count =0
        maxi = 32
        root = None
        def insert(x):
            b= bin(x)[2:]
            b = '0'*(maxi-len(b))+b
            curr = root
            for idx,val in enumerate(b):
                x = int(val)
                if not curr.children[x]:
                    curr.children[x]=Node()
                curr.children[x].count+=1
                curr = curr.children[x]

        def get(x,high):
            x = bin(x)[2:]
            x = '0'*(maxi-len(x))+x
            
            curr = root
            high = bin(high)[2:]
            high = '0'*(maxi-len(high))+high
            count = 0
            for c,h in zip(x,high):
                c = int(c)
                h = int(h)
                xor = c^h
                if h==1:
                    vv = int(not xor) 
                    if curr.children[vv]:
                        count+=curr.children[vv].count
                if not curr.children[xor]:
                    return count
                curr = curr.children[xor]
                # if c==0:
                #     if h==0:
                #         if not curr.children[0]:
                #             return count
                #         curr = curr.children[0]
                #     else:
                #         if curr.children[0]:
                #             count += curr.children[0].count
                #         if not curr.children[1]:
                #             return count
                #         curr= curr.children[1]
                # else:
                #     if h==0:
                #         if not curr.children[1]:
                #             return count
                #         curr = curr.children[1]
                #     else:
                #         if curr.children[1]:
                #             count += curr.children[1].count
                #         if not curr.children[0]:
                #             return count
                #         curr= curr.children[0]
            count += curr.count
            return count

        
        def good(val):
            nonlocal root
            root = Node() # we have to recreate it
            ans= 0
            for x in nums:
                f = get(x,val)
                # print(x,f)
                ans += f
                insert(x)
            # print("over")
            return ans
        return good(high)-good(low-1)