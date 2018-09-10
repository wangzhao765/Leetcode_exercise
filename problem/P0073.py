class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        xlist = []
        ylist = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    if not i in xlist:
                        xlist.append(i)
                    if not j in ylist:
                        ylist.append(j)
        for i in range(len(xlist)):
            for j in range(len(matrix[xlist[i]])):
                matrix[xlist[i]][j]=0
        for j in range(len(ylist)):
            for i in range(len(matrix)):
                matrix[i][ylist[j]]=0

if __name__ == '__main__':
    s = Solution()
    matrix = [[1, 2, 0], [4, 5, 6], [0, 8, 9]]
    s.setZeroes(matrix)
    print(matrix)