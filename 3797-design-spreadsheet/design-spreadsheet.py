class Spreadsheet:

    def __init__(self, rows: int):
        self.d =  collections.Counter()

    def setCell(self, cell: str, value: int) -> None:
        self.d[cell]=value

    def resetCell(self, cell: str) -> None:
        self.d[cell]=0

    def getValue(self, formula: str) -> int:
        ind = formula.index('+')
        x,y = formula[1:ind],formula[ind+1:]
        if not x.isdigit():
            x = self.d[x]
        else:
            x = int(x)
        if not y.isdigit():
            y = self.d[y]
        else:
            y = int(y)
        return x+y


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)