# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # divide at midpoint
        s, f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        
        sec = s.next
        s.next = None

        #reverse sec
        prev = None
        while sec:
            tmp = sec.next
            sec.next = prev
            prev = sec
            sec = tmp
        
        #merge
        fst, sec = head, prev
        while sec:
            tmp1, tmp2 = fst.next, sec.next
            fst.next = sec
            sec.next = tmp1
            fst, sec = tmp1, tmp2
        
