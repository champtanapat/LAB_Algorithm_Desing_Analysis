from collections import deque

stack = deque()
#stack = []
stack.append("https://www.cnn.com/")
stack.append("https://www.cnn.com/world")
stack.append("https://www.cnn.com/india")
stack.append("https://www.cnn.com/china")

print(stack)


stack.pop() #'https://www.cnn.com/china'
print(stack)

stack.pop() #'https://www.cnn.com/india'
print(stack)

stack.pop() #'https://www.cnn.com/world'
print(stack)

stack.pop() #'https://www.cnn.com/'
print(stack)
#stack.pop()
 