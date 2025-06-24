# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res=0
        def dfs(root,su):
            nonlocal res
            if not(root):
                return 
            su = su * 10 + root.val
            if not(root.left) and not(root.right):
                res+=su
                return
            dfs(root.left,su)
            dfs(root.right,su)
        dfs(root,0)
        return(res)