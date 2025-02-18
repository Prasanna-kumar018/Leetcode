class LFUCache:
    class Node:
        def __init__(self,val,c,k):
            self.key = k
            self.count = c
            self.prev = None
            self.next = None
            self.val  = val
        def __str__(self):
            return str(self.count)+" " + str(self.val)+" " + str(self.key)
    curr = 1
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {} # value -> Node
        self.left = {} # count 
        self.right = {} #count 
    def delete(self,node,key):
        prev = node.prev
        prev.next = node.next
        node.next.prev = prev
        del self.map[key]
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        value = self.map[key].val
        node = self.map[key]
        self.delete(node,key)
        node.count+=1
        self.insertit(node.count,node.val,key)
        # for x,y in self.map.items():
        #     print(x,y)
        # print()
        return value

    def insertit(self,c,value,key):
        if c not in self.left:
            l = self.Node(0,0,0)
            r = self.Node(0,0,0)
            l.next = r
            r.prev = l
            self.left[c]=l
            self.right[c]=r
        node = self.Node(value,c,key)
        self.map[key]=node
        prev = self.right[c].prev
        prev.next = node
        node.prev = prev
        self.right[c].prev = node
        node.next = self.right[c]
    def put(self, key: int, value: int) -> None:
        c = 1
        b = True if key not in self.map else False
        if key not in self.map and len(self.map) == self.capacity:
            while self.left[LFUCache.curr].next == self.right[LFUCache.curr]:
                LFUCache.curr+=1
            self.delete(self.left[LFUCache.curr].next,self.left[LFUCache.curr].next.key)
        if key in self.map:
            c = self.map[key].count+1
            self.delete(self.map[key],key)
        self.insertit(c,value,key)
        if b:
            LFUCache.curr=1
        # for x,y in self.map.items():
        #     print(x,y)
        # print()


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)