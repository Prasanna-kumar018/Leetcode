# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        temp = head
        while head:
            n+=1
            head= head.next
        head = temp
        have = n // k
        res = [] 
        rem = n%k
        i = 0
        while i<k:
            if not head:
                res.append(None)
                i+=1
                continue
            t = have+(1 if rem>0 else 0)
            rem-=1
            res.append(head)
            while head and t>1:
                head=head.next
                t-=1
            nxt = head.next
            head.next = None
            head= nxt
            i+=1
        return res
