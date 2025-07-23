# Problem: Lowest Common Ancestor of Deepest Leaves - https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root,depth):
            if not(root):
                return (None,depth)
            left_node,left_depth=dfs(root.left,depth+1)
            right_node,right_depth=dfs(root.right,depth+1)
            if right_depth>left_depth:
                return (right_node,right_depth)
            if right_depth<left_depth:
                return (left_node,left_depth)
            else:
                return (root,left_depth)
        node,_=dfs(root,0)
        return node
            