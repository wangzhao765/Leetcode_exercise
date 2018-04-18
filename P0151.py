class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        wordlist = s.split(" ")
        if len(wordlist)==1:
            return s
        st = wordlist[-1]
        for i in range(len(wordlist)-2, -1, -1):
            if wordlist[i]!="":
                if st=="":
                    st = st + wordlist[i]
                else:
                    st = st + " " + wordlist[i]
        return st

if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("a "))