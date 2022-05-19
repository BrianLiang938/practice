"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not(root):
            return root
        root.next = None
        if root.left and root.right:
            root.left.next = root.right
            root.right.next = None
            s = Solution()
            s.level(root.left)
            s.level(root.right)
        return root
    def level(self, root: 'Optional[Node]'):
        s = Solution()
        if root.left and root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            else:
                root.right.next = None
            s.level(root.left)
            s.level(root.right)