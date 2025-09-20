medical_cause= input("did you have a cause Y or N")
attdance= int(input("enter the attdance"))

if medical_cause=='y':
    print("you are allowed")
else:
    if attdance>=75:
        print("allowed")
        
    else:
        print("not allowed")
    
