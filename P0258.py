class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num==0:
            return 0;
        m = num%9
        if m==0:
            m=9;
        return m

if __name__ == '__main__':
    s = Solution()
    print(s.addDigits(38))