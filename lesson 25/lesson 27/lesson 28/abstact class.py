from abc import ABC,abstractmethod

class absclass(ABC):
    def print(self,x):
        print("passed value",x)
        
        @abstractmethod
        def task(self):
            print("we are inside absclass task")
            
class test_class(absclass):
    def task(self):
        print("we are inside test_class task")
        
obj=test_class()
obj.task()
obj.print(100)