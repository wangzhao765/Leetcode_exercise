class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        i = 1
        while len(matrix)>0:
            a, matrix = Solution.cal(self, matrix, i)
            i = i+1
            if i==5:
                i=1
            ans.extend(a)
        return ans

    def cal(self, matrix, t):
        ans = []
        if t==1:
            ans=matrix[0]
            del(matrix[0])
            return ans, matrix
        elif t==2:
            if len(matrix[0])==1:
                for i in range(len(matrix)):
                    ans.append((matrix[i][0]))
                for i in range(len(matrix)):
                    del(matrix[0])
            else:
                for i in range(len(matrix)):
                    ans.append(matrix[i][-1])
                for i in range(len(matrix)):
                    del (matrix[i][-1])
            return ans, matrix
        elif t==3:
            matrix[-1].reverse()
            ans=matrix[-1]
            del(matrix[-1])
            return ans, matrix
        elif t==4:
            for i in range(len(matrix)-1,-1,-1):
                ans.append(matrix[i][0])
            for i in range(len(matrix)):
                if len(matrix[len(matrix)-1])==1:
                    del(matrix[0])
                else:
                    del(matrix[i][0])
            return ans, matrix

if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]))