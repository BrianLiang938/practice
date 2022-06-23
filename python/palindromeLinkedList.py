# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list = []
        while head:
            list.append(head.val)
            head = head.next
        print(list)
        if list == list[::-1]:
            return 1
        return 0
