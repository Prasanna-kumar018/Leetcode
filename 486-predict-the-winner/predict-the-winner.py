class Solution:
    def predictTheWinner(self, arr: List[int]) -> bool:
        n = len(arr)
        @cache
        def recur(left,right,isalice,val):
            if left>right:
                if val>=0:
                    return 1
                return -1
            res = -1 if isalice else 1
            if isalice:
                res = max(res ,recur(left+1,right,not isalice,val+arr[left]))
                res = max(res, recur(left,right-1,not isalice,val+arr[right]))
            else:
                res = min(res, recur(left+1,right,not isalice,val-arr[left]))
                res = min(res, recur(left,right-1,not isalice,val-arr[right]))
            return res
        x = recur(0,n-1,True,0)
        return True if x==1 else False