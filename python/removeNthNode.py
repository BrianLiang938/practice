# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:       
        current = head
        count = 0
        while current.next:
            count += 1
            current = current.next
        i = count - n
        output = head
        if i < 0:
            return head.next
        for j in range(i):
            output = output.next
        if output.next:
            output.next = output.next.next
        else:
            output.next = None
        return head

