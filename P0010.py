class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        l1=len(s)
        l2=len(p)
        value = [[False for i in range(l2+1)] for j in range(l1+1)]
        value[0][0]=True
        for i in range(l1):
            if s[i]=="*" and value[i-1][0]:
                value[i+1][0]=True
        for i in range(l2):
            if p[i]=="*" and value[0][i-1]:
                value[0][i+1]=True
        for i in range(l1):
            for j in range(l2):
                f=False
                if s[i]=="*":
                    if value[i-1][j+1] or value[i][j+1]:
                        f=True
                    if value[i+1][j] and (s[i-1]==p[j] or s[i-1]=="." or p[j]=="."):
                        f=True
                if p[j]=="*":
                    if value[i+1][j-1] or value[i+1][j]:
                        f=True
                    if value[i][j+1] and (s[i]==p[j-1] or s[i]=="." or p[j-1]=="."):
                        f=True
                if value[i][j]==True:
                    if s[i]==p[j] or s[i]=="." or p[j]==".":
                        f=True
                value[i+1][j+1]=f
        print(value)
        return value[l1][l2]


s=Solution()
print(s.isMatch("", "c*"))