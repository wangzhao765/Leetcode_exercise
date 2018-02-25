class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAXINT = 2147483647
        MININT = -2147483648
        if (divisor == 0) or (dividend == MININT and divisor == -1):
            return MAXINT
        sign = 1
        if (dividend < 0):
            sign = sign * -1
        if (divisor < 0):
            sign = sign * -1
        p = abs(dividend)
        q = abs(divisor)
        s = 0
        while (p >= q):
            t = 1
            r = q
            while (p >= r):
                r = r << 1
                t = t << 1
            p = p - (r >> 1)
            s = s + (t >> 1)
        return s * sign

if __name__ == '__main__':
    a = Solution()
    a.divide(1, 1)