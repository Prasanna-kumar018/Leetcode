class BrowserHistory:

    def __init__(self, homepage: str):
        self.array = [homepage]
        self.pos=0

    def visit(self, url: str) -> None:
        self.pos+=1
        self.array=self.array[0:(self.pos)]
        self.array.append(url)
        # l ===> g ==> fa ==> you ==> 
        

    def back(self, steps: int) -> str:
        self.pos= max(self.pos-steps,0)
        return self.array[self.pos]
        

    def forward(self, steps: int) -> str:
        n = len(self.array)
        self.pos = min(self.pos+steps,n-1)
        return self.array[self.pos]


        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)