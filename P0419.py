class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        ans = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                flag = True
                if board[i][j]!="X":
                    flag = False
                if i>0 and board[i-1][j]=="X":
                    flag = False
                if j>0 and board[i][j-1]=="X":
                    flag = False
                if flag:
                    ans = ans + 1
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.countBattleships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]))