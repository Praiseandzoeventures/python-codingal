from abc import ABC,abstractmethod
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(slef):
        print("i can walk and run")
class dog(animal):
    def move(slef):
        print("i can bark")
class snake(animal):
    def move(slef):
        print("i can crawl")
class snake(animal):
    def move(slef):
        print("i can crawl")
class lion(animal):
    def move(slef):
        print("i can roar")
a=human()
a.move()
b=dog()
b.move()
c=snake()
c.move()
d=lion()
d.move()