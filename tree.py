class N:
    def __init__(self, value):
        self.value = value  
        self.left = None    
        self.right = None   
def build(tokens):
    stack = []
    for token in tokens:
        if token in ('+', '-', '*', '/'):
            root = N(token)
            root.right = stack.pop()
            root.left = stack.pop()
            stack.append(root)
        else:
            stack.append(N(int(token)))
    return stack[0]
def ev(root):
    if root.left is None and root.right is None:
        return root.value, 0  
    leftv, lefto = ev(root.left)
    rightv, righto = ev(root.right)
    if root.value == '+':
        res = leftv + rightv
    elif root.value == '-':
        res = leftv - rightv
    elif root.value == '*':
        res = leftv * rightv
    elif root.value == '/':
        res = leftv / rightv
    total = lefto + righto + 1
    return res, total

