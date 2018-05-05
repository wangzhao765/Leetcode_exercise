# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return Solution.search(self, root, 1)


    def search(self, root, depth):
        if (root == None):
            return depth-1
        return max(Solution.search(self, root.left, depth+1), Solution.search(self, root.right, depth+1))

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    a = TreeNode(9)
    b = TreeNode(20)
    c = TreeNode(15)
    d = TreeNode(7)
    root.left = a
    root.right = b
    b.left = c
    # b.right = d
    print(s.maxDepth(root))