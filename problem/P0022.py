class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []
        for i in range(n+1):
            answer.append([])
        def solution(n):
            if n == 1:
                return ["()"]
            if answer[n-1] == []:
                answer[n-1] = solution(n-1)
            ans = set()
            for st in answer[n-1]:
                ans.add("("+st+")")
            for i in range(n):
                for st1 in answer[i]:
                    for st2 in answer[n-i]:
                        ans.add(st1+st2)
            a = list(ans)
            a.sort()
            return(a)
        answer[n] = solution(n)
        return answer[n]

if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))