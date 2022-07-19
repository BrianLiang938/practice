# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from contextlib import nullcontext


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        found = set()
        while headA:
            found.add(headA)
            headA = headA.next
        while headB:
            if headB in found:
                return headB
            headB = headB.next
        return None