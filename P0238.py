# import copy
# class Solution:
#     def productExceptSelf(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         ans = []
#         l = 0
#         for i in range(len(nums)):
#             ans.append(Solution.search1(self, nums[i]))
#             if len(ans[i])>l:
#                 l = len(ans[i])
#         ansm = []
#         for i in range(l):
#             sum = 0
#             for j in range(len(ans)):
#                 if len(ans[j])>i:
#                    sum = sum + ans[j][i]
#             ansm.append(sum)
#         finalans = []
#         for i in range(len(ans)):
#             ansmt = copy.deepcopy(ansm)
#             for j in range(len(ans[i])):
#                 ansmt[j] = ansmt[j]-ans[i][j]
#             finalans.append(Solution.search2(self, ansmt))
#         return finalans
#
#     def search1(self, num):
#         if num==1:
#             return [0, 1]
#         ans = [0, 0]
#         i = 2
#         n = num
#         while n>1:
#             sum = 0
#             while n>1 and n%i==0:
#                 sum = sum + 1
#                 n = n//i
#             ans.append(sum)
#             i = i+1
#         return ans
#
#     def search2(self, nums):
#         ans = 1;
#         flag = True
#         for i in range(1, len(nums)):
#             if nums[i]>0:
#                 flag = False
#                 for j in range(nums[i]):
#                     ans = ans*i
#         if flag:
#             return 0
#         else:
#             return ans

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums)):
            ans.append(1)
        p = 1
        for i in range(1, len(nums)):
            p = p * nums[i-1]
            ans[i] = ans[i]*p
        p = 1
        for i in range(len(nums)-2, -1, -1):
            p = p * nums[i+1]
            ans[i] = ans[i]*p
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([0, 0]))