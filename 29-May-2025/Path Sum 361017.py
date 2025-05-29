# Problem: Path Sum - https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: 
            return(False)
        if not(root.left) and not(root.right):
            return(root.val == targetSum)
        s1=self.hasPathSum(root.left, targetSum-root.val)
        s=self.hasPathSum(root.right, targetSum-root.val)
        return(s or s1)