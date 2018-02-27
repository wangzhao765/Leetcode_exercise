class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = [[0 for col in range(len(s))] for row in range(len(s))]
        for i in range(len(s)-1):
            if (s[i] == "(" and s[i+1] == ")"):
                ans[i][i+1] = 2
        print(ans)
        for i in range(4,len(s)+2,2):
            for j in range(len(s)-i+1):


if __name__ == '__main__':
    a = Solution()
    a.longestValidParentheses(")()())")