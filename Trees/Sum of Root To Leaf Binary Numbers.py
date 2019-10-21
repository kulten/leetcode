"""
Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most
significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers.
Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
"""
from Trees.helper import make_tree
from Trees.helper import TreeNode


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if not root:
            return 0
        binary_string = ""
        stack = []
        sum = 0
        while stack or root:
            while root:
                binary_string += str(root.val)
                stack.append((root, binary_string))
                root = root.left
            tmproot, binary_string = stack.pop()
            if tmproot:
                if tmproot.left is None and tmproot.right is None:
                    sum += int(binary_string, 2)
            root = tmproot.right
        return sum

"""
Runtime: O(n)
"""
if __name__ == "__main__":
    node_list = [1,0,1,0,1,0,1]
    tree = make_tree(node_list)
    lol = Solution()
    print(lol.sumRootToLeaf(tree))
