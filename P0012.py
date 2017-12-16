class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        n=num
        m=[0,0,0,0]
        for i in range(3, -1, -1):
            m[i]=n%10
            n=n//10
        print(m)
        str=""
        while m[0]>0:
            str += "M"
            m[0] -= 1
        if m[1]==9:
            str += "CM"
        else:
            t=""
            while m[1]>5:
                t += "C"
                m[1] -= 1
            if m[1]==5:
                t = "D"+t
            if m[1]==4:
                str += "CD"
            while m[1]<=3 and m[1]>0:
                t += "C"
                m[1] -= 1
            str += t
        if m[2]==9:
            str += "XC"
        else:
            t=""
            while m[2]>5:
                t += "X"
                m[2] -= 1
            if m[2]==5:
                t = "L"+t
            if m[2]==4:
                str += "XL"
            while m[2]<=3 and m[2]>0:
                t += "X"
                m[2] -= 1
            str += t
        if m[3]==9:
            str += "IX"
        else:
            t=""
            while m[3]>5:
                t += "I"
                m[3] -= 1
            if m[3]==5:
                t = "V" +t
            if m[3]==4:
                str += "IV"
            while m[3]<=3 and m[3]>0:
                t += "I"
                m[3] -= 1
            str +=t
        return(str)



s=Solution()
print(s.intToRoman(3399))