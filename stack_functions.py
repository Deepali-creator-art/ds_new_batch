#To implement a stack operations using user defined functions
#initialize an empty stack
stack=[]
def push(x):
    stack.append(x)
def pop():
    stack.pop()
def size_of_stack():
    size=len(stack)
    return size
def isempty():
    if(len(stack)==0):
        print("Stack is empty")
    else:
        print("Size of stack is",size_of_stack())
def isfull():
    if(len(stack)==3):
        print("Stack is full")
    else:
        print("Stack is empty")
        print("Size of stack is",size_of_stack())
def top_element():
    x=stack[-1]
    return stack.index(x)

push(100)  #function called
pop() #function called
push(200)#function called
push(300)#function called
print("Stack elements are",stack) 
isempty()#function called
pop()#function called
pop()#function called
isempty()#function called
isfull()#function called
push(100)
push(200)
push(300)
isfull()
print(stack)
print(top_element())