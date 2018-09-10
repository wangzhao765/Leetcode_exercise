class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = [[0 for col in range(len(s))] for row in range(len(s))]
        max = 0
        for i in range(len(s)-1):
            if s[i] == "(" and s[i+1] == ")":
                ans[i][i+1] = 1
                max = 2
        for i in range(3, len(s)):
            for j in range(0, len(s)-i):
                if i%2==0:
                    continue
                flag = 0
                if s[j]=="(" and s[j+i]==")" and ans[j+1][j+i-1]==1:
                    flag = 1
                divide = j
                while flag==0 and divide<j+i:
                    if ans[j][divide]==1 and ans[divide+1][j+i]==1:
                        flag = 1
                        break
                    else:
                        divide += 1
                ans[j][i+j] = flag
                if flag==1 and i+1>max:
                    max=i+1
        # max = 0
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         if ans[i][j]==1 and j-i+1>max:
        #             max = j-i+1
        return max

if __name__ == '__main__':
    a = Solution()
    print(a.longestValidParentheses(")(((()))(((())((()))())()())(()((((())))()()(())))((()()(()(((((((()())(())()()))))))))))())(())()((()((())((())(()))(()()(()()()((())((()((()(()))())))(()(()())()()((()(())()()()()()(()(("))