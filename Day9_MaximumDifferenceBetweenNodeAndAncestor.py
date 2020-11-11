'''
Question Description :-
Maximum Difference Between Node and Ancestor

Given the root of a binary tree, find the maximum value V for which there exist different nodes A and B 
where V = |A.val - B.val| and A is an ancestor of B.
A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.

 

Example 1:
                    8
                  /   \ 
                 3     10
                / \     \ 
               1   6     14
                  / \    /
                 4   7  13

    Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
    Output: 7
    Explanation: We have various ancestor-node differences, some of which are given below :
                |8 - 3| = 5
                |3 - 7| = 4
                |8 - 1| = 7
                |10 - 13| = 3
                Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

Example 2:
          1
           \ 
            2
             \ 
              0
            /
           3 

    Input: root = [1,null,2,null,0,3]
    Output: 3
    

Constraints:
    The number of nodes in the tree is in the range [2, 5000].
    0 <= Node.val <= 105
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        
        self.maximum_difference = 0
        
        def helper(root):
            if root is None:
                return 10**6,0
            
            if root.left is None and root.right is None:
                return root.val,root.val
            
            left_min,left_max = helper(root.left)
            right_min,right_max = helper(root.right)
            minimum_value = min(left_min,right_min)
            maximum_value = max(left_max,right_max)
            
            self.maximum_difference = max(self.maximum_difference,abs(root.val-minimum_value),abs(root.val-maximum_value))             
            
            return min(minimum_value,root.val),max(maximum_value,root.val)
        
        helper(root)
        
        return self.maximum_difference
