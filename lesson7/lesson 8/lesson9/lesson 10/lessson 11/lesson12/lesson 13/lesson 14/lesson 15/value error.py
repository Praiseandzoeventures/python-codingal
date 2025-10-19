try:
    number =int(input("enter a number:"))
    print("the number  entered is:")
except ValueError as e:
    print("Exception is",e)