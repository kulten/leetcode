"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root) -> bool:
        previous = float('-inf')
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            tmproot = stack.pop()
            current = tmproot.val
            if previous >= current:
                return False
            previous = current
            root = tmproot.right
        return True


"""
Runtime: O(n)
"""
if __name__ == "__main__":
    tree = TreeNode(5)
    tree.left = TreeNode(1)
    tree.right = TreeNode(3)
    lol = Solution()
    print(lol.isValidBST(tree))
