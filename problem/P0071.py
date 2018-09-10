class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        plist = path.split("/")
        anslist = []
        for i in range(len(plist)):
            if plist[i]=="" or plist[i]==".":
                continue
            elif plist[i]=="..":
                if len(anslist)>0:
                    del(anslist[-1])
            else:
                anslist.append(plist[i])
        s = ""
        for i in range(len(anslist)):
            s = s+"/"+anslist[i]
        if s=="":
            s="/"
        return s

if __name__ == '__main__':
    s = Solution()
    print(s.simplifyPath("/.."))