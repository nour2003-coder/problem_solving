# Problem: Even Odd Tree - https://leetcode.com/problems/even-odd-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import defaultdict
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        d=defaultdict(list)
        if not(self.helper(root,d,0)):
            return(False)
        
        for i in d:
            if i%2==0 and d[i] != sorted(d[i]):
                return(False)
            elif i%2 == 1 and d[i] != sorted(d[i],reverse=True) :
                return(False)
            elif len(set(d[i])) !=len(d[i]):
                return(False)
        return(True)
    def helper(self,root,d,level):
        if not(root):
            return(True)
        if level % 2 != (root.val+1)%2:
            return(False)
        else:
            d[level].append(root.val)
            return(self.helper(root.left,d,level+1) and self.helper(root.right,d,level+1) )  
         
        