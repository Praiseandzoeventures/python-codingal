string=input("please enter the word")

char=input("please enter your character ")

i=0
count=0

while i<len(string):
    if string[i]==char:
        count=count+1
    i=i+1
    
print("the character occurence is:",count)
