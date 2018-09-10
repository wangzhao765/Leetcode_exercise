class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits=="":
            return([])
        charlist=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        l=len(digits)
        num=[]
        for i in range(l):
            num.append(len(charlist[ord(digits[i])-ord("0")]))
        num.append(2)
        s=[0 for i in range(l+1)]
        ans=[]
        while s[l]==0:
            str=""
            for i in range(l):
                str += charlist[ord(digits[i])-ord("0")][s[i]]
            ans.append(str)
            s[0] += 1
            i=0;
            while s[i]==num[i]:
                s[i]=0
                i += 1
                s[i] += 1
        return(ans)

s=Solution()
print(s.letterCombinations(""))