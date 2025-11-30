class myclass:
    
    __privateVar=27
    
    def __privmeth():
            print("i am inside class myclass")
        
    def hello(self):
            print("private varialbe value :",myclass.__privateVar)
        
foo=myclass()
foo.hello()
foo.__privateVar=28
foo.hello()