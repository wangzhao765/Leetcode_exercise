class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s=str
        flag=False
        if s=="":
            return(0)
        p=0
        while p<len(s) and s[p]==" ":
            p += 1
        if p==len(s):
            flag=True
        if not(s[p]=="+" or s[p]=="-" or (s[p]>="0" and s[p]<="9")):
            flag=True
        if flag:
            return(0)
        f=1
        if s[p]=="+":
            p += 1
        else:
            if s[p]=="-":
                f=0
                p += 1
        if p==len(s):
            return(0)
        sum=0
        while p<len(s) and (s[p]>="0" and s[p]<="9"):
            c=ord(s[p])-48
            if sum==214748364:
                if c>7 and f==1:
                    return 2147483647
                if c>8 and f==0:
                    return -2147483648
            if sum>214748364:
                if f==1:
                    return 2147483647
                else:
                    return -2147483648
            sum = sum*10+c
            p += 1
        if f==0:
            sum = 0-sum
        return(sum)



s=Solution()
print(s.myAtoi("      -11919730356x"))