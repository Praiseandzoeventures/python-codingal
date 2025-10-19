try:
    num1,num2=eval(input("enter two numbers separted by comma:"))
    result =num1/num2
    print("the result is :")
except ZeroDivisionError :
    print("division by zero is error")
except SyntaxError :
    print("comma is missing enter numbers separated by comma like this  5 ,8")
except:
    print("worng input")
    
else:
    print("no exceptions")
finally:
    print("this will execute no matter what")