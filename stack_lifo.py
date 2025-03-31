from queue import LifoQueue
stack=LifoQueue(maxsize=5)
#to add element into a stack
stack.put(10)
print(stack)
stack.put(20)
stack.put(30)
print(stack.qsize())
print(stack.empty())
print(stack.full())
stack.put(40)
stack.put(50)
print(stack.full())
stack.get(40)
stack.put_nowait(60)
print(stack)