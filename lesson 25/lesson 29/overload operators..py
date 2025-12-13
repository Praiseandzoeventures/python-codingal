class A:
    def __init__(self,a):
        self.a=a
    def __lt__(self,other):
        if (self.a<other.a):
            return "ob1 is less than ob2"
        else:
            return "ob2 is less than ob1"
    def __eq__(self, other):
        if (self.a==other.a):
            return "Both are equal"
        else:
            return "Not equal"
        
ob1=A(2)
ob2=A(3)

print(ob1<ob2)
print(ob1==ob2)