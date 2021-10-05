# URL : https://leetcode.com/problems/valid-parentheses/submissions/
class Solution:
    def isValid(self, s: str) -> bool:
        di={'{':'}','[':']','(':')'}
        stack=[]
        for x in s:
            if x in ['(','[','{']:
                stack.append(x)
            else:
                if not stack or di[stack.pop()]!=x:
                        return False
        return len(stack)==0