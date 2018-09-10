class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0 or x==10:
            return False
        l=0
        a=x
        b=0
        while x>0:
            l += 1
            x = x//10
        if l<2:
            return True
        for i in range(l//2):
            b=b*10+a%10
            a=a//10
        if (a==b) or (b==a//10):
            return True
        else:
            return False



s=Solution()
print(s.isPalindrome(1234421))