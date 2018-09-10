class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        wordl = len(words[0])
        wordnum = len(words)
        l = wordl * wordnum
        t = len(s) - l
        ans = []
        for i in range(t+1):
            str = s[i:i+l]
            w = words.copy()
            flag = True
            for j in range(0,l,wordl):
                tempstr = str[j:j + wordl]
                if (tempstr in w):
                    w.remove(tempstr)
                else:
                    flag = False
                    break
            if (flag):
                ans.append(i)
        return ans


if __name__ == '__main__':
    a = Solution()
    a.findSubstring("barfoothefoobarman", ["foo", "bar"])