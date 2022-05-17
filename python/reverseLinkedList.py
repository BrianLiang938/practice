# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not(head):
            return head
        output = ListNode(head.val)
        head = head.next
        while head:
            temp = ListNode(head.val, output)
            output = temp
            head = head.next
        return output

#recursion
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not(head):
            return head
        output = ListNode(head.val)
        output = recusionReverse(output, head)
        return output
    def recursionReverse(self, curr: Optional[ListNode], list: Optional[ListNode]) -> Optional[ListNode]:
        if not(list):
            return curr
        list = list.next
        temp = ListNode(list.val, recursionReverse(curr, list))
        curr = temp
        return curr
        
        
        