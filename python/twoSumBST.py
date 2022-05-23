# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        vals = set()
        return self.recur(root, vals, k)
    def recur(self, root, set, k):
        if root == None:
            return 0
        if root.val in set:
            return 1
        else:    
            set.add(k - root.val)
        return self.recur(root.left, set, k) or self.recur(root.right, set, k)