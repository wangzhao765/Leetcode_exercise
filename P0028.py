class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)

if __name__ == '__main__':
    a = Solution()
    i = a.strStr("hello", "ll")
    j = a.strStr("aaaaa", "bba")
    print(i, j)