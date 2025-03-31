def infixtopostfix(expression):
    #F+D-C*(B+A)
    stack=[]
    output_expression=''
    for char in expression:
        if char not in operators:
            output_expression+=char #output_expression=output_expression+char
        elif char=='(':  
            stack.append('(')
        elif char==')':
            while stack and stack[-1]!= '(':
                output_expression+=stack.pop()
            stack.pop()
        else:
            while stack and stack[-1]!='(' and precendence[char]<=precendence[stack[-1]]:
                output_expression+=stack.pop()
            stack.append(char) 
    while stack:
        output_expression+=stack.pop()
    return output_expression
        
expression='(A+B)*C-D+F'
reverse_expression=expression[::-1]
print("Reverse string",reverse_expression)
reverse_expression=reverse_expression.replace('(',')',1)
reverse_expression=reverse_expression.replace(')','(',1)
print("Final reverse string",reverse_expression)
operators = set(['+', '-', '*', '/', '(', ')'])  # set of operators
precendence = {'+':1, '-':1, '*':2, '/':2}
postfix_expression=infixtopostfix(reverse_expression) #function call
print("Postfix expression is",postfix_expression)
#convert postfix to prefix
prefix_expression=postfix_expression[::-1]
print("Prefix expression is",prefix_expression)