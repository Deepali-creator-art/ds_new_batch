from queue import deque
s1=deque()
print(type(s1))
#append() is used to perform stack operation
s1.append(10)
print(s1)
s1.append(20)
s1.append(30)
s1.append(40)
print(s1)
#pop() is used to remove last element.
s1.pop()
print(s1)
