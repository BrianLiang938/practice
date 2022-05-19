# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        s = Solution()
        output = []
        if root:
            s.recur(root, output)
        return output
    def recur(self, root, output):
        s = Solution()
        if root.left != None:
            s.recur(root.left, output)
        output.append(root.val)
        if root.right != None:
            s.recur(root.right, output)