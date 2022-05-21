# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> List[List[int]]:
        s = Solution()
        output = 0
        temp = [[root]]
        if root:
            output = 1
            output = s.recur(temp)
        return output
    def recur(self, input) -> int:
        s = Solution()
        temp = []
        for n in input[-1]:
            if n.left != None:
                temp.append(n.left)
            if n.right != None:
                temp.append(n.right)
        if len(temp) > 0:
            input.append(temp)
            return s.recur(input) + 1
        else:
            return 1
