# class Solution:
#     def countPrimes(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         prime = [2]
#         if n<=2:
#             return 0
#         for i in range(3, n):
#             flag =True
#             for j in prime:
#                 if i%j==0:
#                     flag = False
#                     break
#             if flag:
#                 prime.append(i)
#         return len(prime)

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return 0
        prime = []
        for i in range(n):
            prime.append(1)
        for i in range(2, n):
            if prime[i]==0:
                continue
            for j in range(i*2, n, i):
                prime[j]=0
        prime[0]=0
        prime[1]=0
        return sum(prime)

if __name__ == '__main__':
    s = Solution()
    print(s.countPrimes(499979))