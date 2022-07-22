# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        under = ListNode()
        over = ListNode()
        oHead = over
        out = under
        while head:
            if head.val < x:
                temp = ListNode(head.val)
                under.next = temp
                under = under.next            
            else:
                temp = ListNode(head.val)
                over.next = temp
                over = over.next
            head = head.next
        under.next = oHead.next
        return out.next