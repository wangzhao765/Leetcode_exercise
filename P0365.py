# class Solution:
#     def canMeasureWater(self, x, y, z):
#         """
#         :type x: int
#         :type y: int
#         :type z: int
#         :rtype: bool
#         """
#         ans = []
#         a = max(x,y)
#         b = min(x,y)
#         if z==0:
#             return True
#         if z>a+b:
#             return False
#         if b==0:
#             if a==z:
#                 return True
#             else:
#                 return False
#         flag = True
#         while flag:
#             mod = a%b
#             if (z%b)==mod:
#                 return True
#             if not mod in ans:
#                 ans.append(mod)
#                 a = x-(y-mod)
#             else:
#                 flag=False
#         if (z%b) in ans:
#             return True
#         else:
#             return False

class Solution:
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z==0:
            return True
        if z<=x+y and z%Solution.gcd(self, x,y)==0:
            return True
        else:
            return False

    def gcd(self, x, y):
        if y==0:
            return x
        else:
            return Solution.gcd(self, y, x%y)

if __name__ == '__main__':
    s = Solution()
    print(s.canMeasureWater(2,6,5))