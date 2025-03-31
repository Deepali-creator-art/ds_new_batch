#Using list implement a stack
stack=[] #initialize an empty list
#add elements into a stack (push operation)
stack.append('Pratham')
print("Stack elements are",stack)
stack.extend(['Pratiksha','Sarvesh'])
print("Stack elements are",stack)
#remove elements from a stack(pop operation)
stack.pop()
print("Stack elements are",stack)
print("Size of stack is",len(stack))