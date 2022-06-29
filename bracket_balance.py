def Pairs(open,close):
    if open=='[' and close==']':
        return True
    if open=='{' and close=='}':
        return True
    if open=='(' and close==')':
        return True
    return False
def Balanced(exp):
    stack=[]
    for i in range(len(exp)):
        if exp[i]=='[' or exp[i]=='{' or exp[i]=='(':
            stack.append(exp[i])
        elif exp[i] == ']' or exp[i] == '}' or exp[i] == ')':
            if Pairs(stack[-1],exp[i]):
                stack.pop()
            else:
                return False
    if len(stack)==0:
        return True
    else:
        return False

exp= "[]()({}){{}}[][]()"
r= Balanced(exp)
if r==True:
    print("Balanced")
else:
    print("Not Balanced")