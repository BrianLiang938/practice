# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return None
        return self.dfs(root, val)
    def dfs(self, root, val):
        if root == None:
            return None
        if root.val == val:
            return root
        elif root.val > val:
            return self.dfs(root.left, val)
        elif root.val < val:
            return self.dfs(root.right, val)
        else:
            return None
