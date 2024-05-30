class queue:
    def __init__(self):
        self.values=[]
    def enqueue(self,x):
        self.values.append(x)
    def dequeue(self):
        return self.values.pop(0)
    def printqueue(self):
        print(self.values)
s=queue()
s.enqueue(10)
s.enqueue(20)
s.enqueue(30)
s.printqueue()
s.dequeue()
s.printqueue()
