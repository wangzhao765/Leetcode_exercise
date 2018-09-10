class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i1=m-1
        i2=n-1
        i=m+n-1
        while i>=0:
            if i1<0:
                nums1[i]=nums2[i2]
                i2=i2-1
                i=i-1
            elif i2<0:
                nums1[i]=nums1[i1]
                i1=i1-1
                i=i-1
            elif nums1[i1]<=nums2[i2]:
                nums1[i]=nums2[i2]
                i2=i2-1
                i=i-1
            else:
                nums1[i]=nums1[i1]
                i1=i1-1
                i=i-1

if __name__ == '__main__':
    s = Solution()
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    m=3
    n=3
    s.merge(nums1,m,nums2,n)
    print(nums1)