def cube(number):
    return number*number*number

def divisible_by_three(number):
    if number %  3==0:
        return cube(number)
    else:
        return False
    
    
print(divisible_by_three(9))
print(divisible_by_three(4))