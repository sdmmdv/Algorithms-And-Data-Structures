#!/usr/bin/env python3
from stack import Stack

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = Stack()
        for ind in range(len(s)):
            elem = ''
            if s[ind] in '([{':
                stack.push(s[ind])
            elif not stack.empty():
                elem = stack.pop()
            else:
                return False
            
            if (s[ind] in ')' and elem != '(') \
                or (s[ind] in '}' and elem != '{') \
                or (s[ind] in ']' and elem != '['):
                return False
        return stack.empty()

solution = Solution()
print(solution.isValid("()[]{}"))
print(solution.isValid("({})[]{}{"))
print(solution.isValid(""))
print(solution.isValid("({[{()}]})"))

