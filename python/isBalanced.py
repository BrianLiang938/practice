# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return 1
        left = right = 0
        if root.left:
            left = self.helper(root.left, 1)
        if root.right:
            right = self.helper(root.right, 1)
        print(root.val, left, right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return False
        return True
        
    def helper(self, root, height) -> int:
        left = right = height
        if root.left:
            left = self.helper(root.left, height + 1)
        if root.right:
            right = self.helper(root.right, height + 1)
        print(root.val, left, right)
        if abs(left - right) > 1 or (left == -1 or right == -1):
            return -1
        return max(left,right)
