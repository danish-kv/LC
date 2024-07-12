class Solution:
    def isValid(self, s: str) -> bool:
        mydict = {
            '(' : ')',
            '{' : '}',
            '[' : ']',
        }
        stack = []
        for i in s:
            if i in mydict:
                stack.append(i)
            elif len(stack) < 1 or i != mydict[stack.pop()]:
                return False
                
        return len(stack) == 0
