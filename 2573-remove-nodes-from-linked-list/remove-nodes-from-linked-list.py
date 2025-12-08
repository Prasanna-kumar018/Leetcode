# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(root):
            prev = None
            while root:
                nxt = root.next
                root.next = prev
                prev = root
                root = nxt
            return prev
        
        node = reverse(head)
        head = ListNode(0)
        tail = head
        prev = -10**10
        while node:
            if node.val>=prev:
                head.next = node
                head = head.next
                prev = node.val
            node = node.next
        head.next = None
        return reverse(tail.next)