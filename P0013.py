class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num=[]
        for i in range(len(s)):
            if s[i]=="I":
                num.append(1)
            if s[i]=="X":
                num.append(10)
            if s[i]=="C":
                num.append(100)
            if s[i]=="M":
                num.append(1000)
            if s[i]=="V":
                num.append(5)
            if s[i]=="L":
                num.append(50)
            if s[i]=="D":
                num.append(500)
        sum=0;
        for i in range(len(num)):
            if i==len(num)-1:
                sum += num[i]
            else:
                if num[i]<num[i+1]:
                    sum -= num[i]
                else:
                    sum += num[i]
        return(sum)



s=Solution()
print(s.romanToInt("MCMLXXX"))