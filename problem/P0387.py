class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        alphabeta = "abcdefghijklmnopqrstuvwxyz"
        sum = []
        for i in range(26):
            sum.append(s.count(alphabeta[i]))
        for i in range(len(s)):
            if sum[alphabeta.index(s[i])]==1:
                return i
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.firstUniqChar("leetcode"))