class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        flag = True
        l = 0
        r = len(s)-1
        while flag and l<r:
            while l<len(s) and (not s[l].isalpha() and not s[l].isdigit()):
                l = l+1
            while r>=0 and (not s[r].isalpha() and not s[r].isdigit()):
                r = r-1
            if l<r:
                if s[l].capitalize()==s[r].capitalize():
                    l = l+1
                    r = r-1
                else:
                    flag = False
        return flag

if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome("0P"))