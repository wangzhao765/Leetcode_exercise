class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s1 = int(len(nums) * (len(nums) + 1) / 2)
        s2 = sum(nums)
        return s1-s2

if __name__ == '__main__':
    s = Solution()
    print(s.missingNumber([9,6,4,2,3,5,7,0,1]))