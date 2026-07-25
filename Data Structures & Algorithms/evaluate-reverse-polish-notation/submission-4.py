class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        symbols = {'+','-','*','/'}
        for c in tokens:
                if c in symbols:
                    b = stack.pop()
                    a = stack.pop()
                    if c=='+':
                        res = a+b
                    elif c=='-':
                        res = a-b
                    elif c=='*':
                        res = a*b
                    elif c=='/':
                        res = int(a/b)
                    else:
                        pass
                    stack.append(res)
                else:
                    stack.append(int(c))
        return stack.pop()
