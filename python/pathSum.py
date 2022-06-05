# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None: return 0
        return self.dfs(root, 0, targetSum)
    def dfs(self, root, sum, target) -> bool:
        left = 0
        right = 0
        sum = sum + root.val
        if root.left != None:
            left = self.dfs(root.left, sum, target)
        if root.right != None:
            right = self.dfs(root.right, sum, target)
        if root.right == None and root.left == None:
            if sum == target:
                return 1
            else:
                return 0
        return left or right
