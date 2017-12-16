class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a=x
        b=0
        if a>0:
            f=1
        else:
            f=0
            a=0-x
        while a>0 and b<=214748364:
            if b==214748364 and a>7:
                if not(a==8 and f==0):
                    return 0
            b = b*10+a%10
            a = a//10
        if a>0:
            return 0
        if f==1:
            return b
        else:
            return 0-b


s=Solution()
print(s.reverse(1000000003))
#7463847412