# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        queue = []
        queue.append([root, 0])
        index = 0
        level = 0
        ans = []
        while index<len(queue):
            ansl = []
            while index<len(queue) and queue[index][1]==level:
                if queue[index][0].left!=None:
                    queue.append([queue[index][0].left, queue[index][1]+1])
                if queue[index][0].right!=None:
                    queue.append([queue[index][0].right, queue[index][1]+1])
                ansl.append(queue[index][0].val)
                index = index + 1
            ans.append(ansl)
            level = level + 1
        return ans

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
    b.right = d
    print(s.levelOrder(root))