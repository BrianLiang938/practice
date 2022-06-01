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
    def connect(self, root: 'Node') -> 'Node':
        stack = []
        if root != None:
            stack.append(root)
            self.dfs(stack)
        return root

    def dfs(self, stack):
        n = len(stack)
        first = stack.pop(0)
        newStack = []
        for m in range(n):
            if first.left != None:
                newStack.append(first.left)
            if first.right != None:
                newStack.append(first.right)
            if len(stack) > 0:
                first.next = stack.pop(0)
                first = first.next
            else:
                first.next = None
        if len(newStack) > 0:
            self.dfs(newStack)
