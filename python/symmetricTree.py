# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return 1
        else:
            return self.recur(root.left, root.right)
    def recur(self, left, right):
        if left == None and right == None:
            return 1
        elif left == None or right == None:
            return 0
        elif left.val == right.val:
            outside = self.recur(left.left, right.right)
            inside = self.recur(left.right, right.left)
            return outside and inside
        else:
            return 0
