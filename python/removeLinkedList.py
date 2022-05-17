# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:       
        dummy = head       
        while dummy and dummy.val == val:
            dummy = dummy.next
        if not(dummy):
            return dummy
        if dummy.next:
            curr = dummy.next
            temp = dummy
            while curr:
                if curr.val == val:
                    temp.next = curr.next
                    curr = temp.next
                else:
                    curr = curr.next
                    temp = temp.next
        return dummy