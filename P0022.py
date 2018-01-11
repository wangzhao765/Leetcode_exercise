class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def solution(n):
            if n == 1:
                return ["()"]
            ans_set = set()
            s = solution(n-1)
            for st in s:
                ans_set.add("()"+st)
                ans_set.add("("+st+")")
                ans_set.add(st+"()")
            return list(ans_set)
        s = solution(n)
        s1 = s.sort()
        return s

if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))