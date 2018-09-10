# class Solution:
#     def checkInclusion(self, s2, s1):
#         """
#         :type s1: str
#         :type s2: str
#         :rtype: bool
#         """
#         if s2=="":
#             return True
#         if len(s1)<len(s2):
#             return False
#         for i in range(len(s1)-len(s2)+1):
#             if Solution.search(self, s1[i:i+len(s2)], s2):
#                 return True
#         return False
#
#     def search(self, s1, s2):
#         for i in range(len(s1)):
#             index = s2.find(s1[i])
#             if index>=0:
#                 s2 = s2[0:index]+s2[index+1:len(s2)]
#             else:
#                 return False
#         return True

class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1=="":
            return True
        if len(s1)>len(s2):
            return False
        hashs1 = Solution.h(self, s1)
        for i in range(len(s2)-len(s1)+1):
            hashs2 = Solution.h(self, s2[i:i+len(s1)])
            if hashs1==hashs2:
                return True
        return False

    def h(self, s):
        ans = []
        for i in "abcdefghijklmnopqrstuvwxyz":
            ans.append(s.count(i))
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.h("abc"))
    print(s.checkInclusion("ab", "ab"))