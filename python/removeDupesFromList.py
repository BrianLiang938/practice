# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not(head) or not(head.next):
            return head
        output, dummy, curr = head, head, head.next
        while dummy and curr:
            if curr.val == dummy.val:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next
            curr = curr.next
        return output