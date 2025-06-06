# Problem: Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return(self.helper(root,-float('inf'),float('inf')))
    def helper(self,root,min_,max_):
        if not(root):
            return(True)
        if not(min_< root.val< max_):
            return(False)
        return(self.helper(root.left,min_,root.val) and self.helper(root.right,root.val,max_))