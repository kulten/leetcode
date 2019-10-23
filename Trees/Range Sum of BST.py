"""
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.



Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
"""
from Trees.helper import TreeNode, make_tree


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        stack = [root]
        total = 0
        while stack:
            node = stack.pop()
            if node:
                if L <= node.val <= R:
                    total += node.val
                if L < node.val:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
        return total


"""
Runtime: O(n)
"""
if __name__ == "__main__":
    node_list = [10,5,15,3,7,13,18,1,None,6]
    L = 6
    R = 10
    lol = Solution()
    tree = make_tree(node_list)
    print(lol.rangeSumBST(tree, L, R))
