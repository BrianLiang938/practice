# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sorted = ListNode(0, None)
        min = sorted = curr = head
        while curr.next:
            if curr.next.val < min.val:
                min = curr.next
            sorted.next = min
            curr = curr.next
        
        