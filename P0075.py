class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        Solution.qsort(self, 0, len(nums)-1, nums)

    def qsort(self, p, q, nums ):
        if p>=q:
            return
        l=p
        r=q
        m=nums[(p+q)//2]
        while l<r:
            while nums[l]<m:
                l=l+1
            while nums[r]>m:
                r=r-1
            if l<=r:
                t=nums[l]
                nums[l]=nums[r]
                nums[r]=t
                l=l+1
                r=r-1
        if p<r:
            Solution.qsort(self, p, r, nums)
        if l<q:
            Solution.qsort(self, l, q, nums)


if __name__ == '__main__':
    s = Solution()
    l = [0, 1]
    s.sortColors(l)
    print(l)