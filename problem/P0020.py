class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        l=len(s)
        i=0
        for i in range(l):
            if s[i]==")":
                if stack==[]:
                    return False
                if stack[-1]=="(":
                    stack.pop(-1)
                else:
                    return False
            elif s[i]=="]":
                if stack==[]:
                    return False
                if stack[-1]=="[":
                    stack.pop(-1)
                else:
                    return False
            elif s[i]=="}":
                if stack==[]:
                    return False
                if stack[-1]=="{":
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(s[i])
        if stack==[]:
            return True
        else:
            return False

s=Solution()
print(s.isValid("([]){}"))