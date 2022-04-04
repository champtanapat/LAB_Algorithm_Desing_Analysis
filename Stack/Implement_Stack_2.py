from mimetypes import init


class Stack:
    def __init__(self) :
        self.container = []
    
    def push(self,val):
        self.container.append(val)
    
    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def isEmpty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)
        
def main():
    s = Stack()
    print(s.isEmpty())
    s.push(99)
    s.push(10)
    s.push(5)
    s.push(88)
    print(s.container)


if __name__=="__main__":
    main()

