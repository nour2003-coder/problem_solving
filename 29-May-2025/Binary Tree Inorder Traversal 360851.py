# Problem: Binary Tree Inorder Traversal - https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        self.help_funct(root,res)
        return res
    def help_funct(self,root,res):
        if root:
            self.help_funct(root.left,res)
            res.append(root.val)
            self.help_funct(root.right,res)