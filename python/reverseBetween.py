# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        out = ListNode(head.val)
        while curr and curr.val != left:
            out.val = curr.val
            out.next = ListNode()
            curr = curr.next
        if curr == None:
            return head
        temp = ListNode()
        end = temp
        while curr.val != right:
            if curr == None:
                return head
            temp.val = curr.val
            new = ListNode(-1, temp)
            temp = new
            curr = curr.next
        temp.val = curr.val
        post = ListNode()
        while curr:
            post.val = curr.val
            post.next = ListNode()
            curr = curr.next
        post.next = None
        end.next = post
        out.next = temp
        return out