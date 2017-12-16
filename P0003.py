class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        v = [1]
        max = 1
        for i in range(1, len(s), 1):
            #print(s[i])
            j = i-1;
            while s[j] != s[i]:
                j -= 1
            v.append(min(v[i-1]+1, (i-j)))
            if v[i] > max:
                max = v[i]
        return max

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))