class stack:
    def __init__(self):
        self.values=[]
    def push(self,x):
        self.values.append(x)
    def pop(self):
        return self.values.pop()
    def printStack(self):
        print(self.values)
#values=[]
s=stack()
s.push(10)
s.push(20)
s.push(30)
s.printStack()
print(s.pop())
s.printStack()
