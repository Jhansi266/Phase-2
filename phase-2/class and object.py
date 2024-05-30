class student1:
    def __init__(self,name,rollno,maths,sci,python,social,java):
        self.name=name
        self.rollno=rollno
        self.maths=maths
        self.sci=sci
        self.python=python
        self.social=social
        self.java=java
    def member(self):
        print(self.name)
        print(self.rollno)
        print(self.sci)
        print(self.python)
        print(self.social)
        print(self.java)
obj=student1("sravya",665,23,52,55,52,85)
obj.member()
obj1=student1("navya",678,53,26,75,52,52)
obj1.member()
obj3=student1("pooja",755,52,35,62,75,95)
obj3.member()
