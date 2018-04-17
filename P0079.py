import copy
class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        path = []
        for i in range(len(board)):
            a = []
            for j in range(len(board[0])):
                a.append(0)
            path.append(a)
        ans = False
        for i in range(len(board)):
            if ans:
                break
            for j in range(len(board[0])):
                p = copy.deepcopy(path)
                if board[i][j]==word[0]:
                    ans = ans or Solution.search(self, board, word, i, j, 0, p)
                if ans:
                    break
        return ans

    def search(self, board, word, x, y, i, path):
        # print(x,y,i)
        # if [x,y,i]==[2,2,6]:
        #     print(path)
        if path[x][y]==1:
            return False
        if board[x][y]==word[i]:
            p=copy.deepcopy(path)
            p[x][y]=1
            if i==len(word)-1:
                return True
            else:
                flag = False
                if x!=0:
                    flag = flag or Solution.search(self, board, word, x-1, y, i+1, p)
                if x!=len(board)-1:
                    flag = flag or Solution.search(self, board, word, x+1, y, i+1, p)
                if y!=0:
                    flag = flag or Solution.search(self, board, word, x, y-1, i+1, p)
                if y!=len(board[0])-1:
                    flag = flag or Solution.search(self, board, word, x, y+1, i+1, p)
                return flag
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    matrix = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
    matrix = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
    matrix = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
    word = "ABCESEEEFS"
    # word = "AAB"
    print(s.exist(matrix, word))