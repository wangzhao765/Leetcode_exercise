# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder)==0:
            return None
        else:
            return Solution.search(self, inorder, postorder, 0, len(inorder)-1, 0, len(postorder)-1)

    def search(self, inorder, postorder, li, ri, lp, rp):
        if li>ri:
            return None
        if li==ri:
            return TreeNode(inorder[li])
        i = inorder.index(postorder[rp])
        print(li, ri, lp, rp, i)
        root = TreeNode(postorder[rp])
        root.left = Solution.search(self, inorder, postorder, li, i-1, lp, lp+(i-li)-1)
        root.right = Solution.search(self, inorder, postorder, i+1, ri, lp+(i-li), rp-1)
        return root

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
    inorder = [2,3,1]
    postorder = [3,2,1]
    root = s.buildTree(inorder, postorder)
    print(s.levelOrder(root))