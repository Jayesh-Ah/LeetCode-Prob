# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def PathSum(node):
            if node is None:
                return 0
            left = max(0, PathSum(node.left))
            right = max(0, PathSum(node.right))
            self.NodeSum = max(self.NodeSum, node.val + right + left)
            return node.val + max(left, right)
        self.NodeSum = float('-inf')
        PathSum(root)
        return self.NodeSum
        
