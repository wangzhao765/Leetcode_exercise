class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        s1 = nums1
        s2 = nums2
        l1 = len(s1)
        l2 = len(s2)
        if (l1+l2) % 2 == 1:
            k = (l1+l2) // 2 + 1
            f = 1
        else:
            k = (l1+l2) // 2
            f = 0

        while l1 > 0 and l2 > 0 and k > 1:
            p = min(k//2-1, l1-1, l2-1)
            if s1[p] > s2[p]:
                s2 = s2[p+1:l2]
                l2 = len(s2)
                k -= (p+1)
            else:
                s1 = s1[p+1:l1]
                l1 = len(s1)
                k -= (p+1)
        if l1 == 0:
            if f == 0:
                return (s2[k-1]+s2[k])/2.0
            else:
                return s2[k-1]
        if l2 == 0:
            if f == 0:
                return (s1[k-1]+s1[k])/2.0
            else:
                return s1[k-1]
        if k == 1:
            if f == 1:
                return min(s1[0], s2[0])
            else:
                if l1 == 1:
                    if l2 == 1:
                        return (s1[0]+s2[0])/2.0
                    else:
                        return (s2[0]+min(s1[0], s2[1]))/2.0
                if l2 == 1:
                    return min(s2[0]+s1[0], s1[0]+s1[1])/2.0
                return min(s1[0]+min(s1[1], s2[0], s2[1]), s2[0]+min(s2[1], s1[0], s1[1]))/2.0

s=Solution()
print(s.findMedianSortedArrays([3], [1, 2, 4, 5]))