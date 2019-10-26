"""
Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST.
Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion.
You can return any of them.

For example,

Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
"""
from Trees.helper import make_tree, TreeNode


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        def insert(node,val):
            if node.val > val:
                if not node.left:
                    node.left = TreeNode(val)
                else:
                    insert(node.left, val)
            else:
                if not node.right:
                    node.right = TreeNode(val)
                else:
                    insert(node.right, val)
            return node
        root = insert(root, val)
        return root


"""
Runtime: O(n)
"""
if __name__ == "__main__":
    nodes = [4,2,7,1,3]
    val = 5
    tree = make_tree(nodes)
    lol = Solution()
    print(lol.insertIntoBST(tree, val))
