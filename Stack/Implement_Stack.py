from collections import deque

class Stack:
  def __init__(self):
    self.container = deque()

  def push(self,val):
    self.container.append(val)

  def pop(self):
    return self.container.pop()

  def peek(self):
    return self.container[-1]

  def is_empty(self):
    return len(self.container)==0

  def size(self):
    return len(self.container)




def main():
    x = Stack()
    print("Stack is empty: ", x.is_empty())
    #ใส่ไปตรงๆ
    x.container.append("Test1")
    x.container.append("Test2")
    print(x.container)
    x.container.pop()
    print(x.container)


    s = Stack()
    print("Stack is empty: ",s.is_empty())
    #ใส่ข้อมูลผ่าน function 
    s.push(5)
    print(s.container)
    print(s.pop())
    print(s.container)
    print(s.is_empty())

    # s.push(9)
    # s.push(34)
    # s.push(78)
    # s.push(12)
    # print(s.container)

    # s.peek()

    # print(s.pop())
    # print(s.pop())
    # print(s.pop())
    # print(s.pop())
    # print(s.is_empty())


if __name__=="__main__":
    main()
