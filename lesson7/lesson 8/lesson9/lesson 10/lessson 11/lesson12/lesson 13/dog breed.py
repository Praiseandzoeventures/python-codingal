class dog:
    def __init__(self,name,breed,age):
        self.name=name
        self.breed=breed
        self.age=age
        
        dog1=dog("buddy,golden retriever",5)
        dog2=dog("max,beagle",3)
        
print(dog.name,"is",dog.age,"years old")
print(dog.name," is",dog.age,"years old")