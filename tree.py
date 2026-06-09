class Node:
    def __init__(self, value):
        self.value = value  
        self.left = None    
        self.right = None   
def build_expression_tree(tokens):
    stack = []
    for token in tokens:
        if token in ('+', '-', '*', '/'):
            root = Node(token)
            root.right = stack.pop()
            root.left = stack.pop()
            stack.append(root)
        else:
            stack.append(Node(int(token)))
    return stack[0]
def evaluate(root):
    if root.left is None and root.right is None:
        return root.value, 0  
    left_val, left_ops = evaluate(root.left)
    right_val, right_ops = evaluate(root.right)
    if root.value == '+':
        result = left_val + right_val
    elif root.value == '-':
        result = left_val - right_val
    elif root.value == '*':
        result = left_val * right_val
    elif root.value == '/':
        result = left_val / right_val
    total_ops = left_ops + right_ops + 1
    return result, total_ops

