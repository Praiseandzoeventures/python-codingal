import random
import time
number=random.randint(1,100)
def intro():
    print("may i ask you for your name?")
    global name
    name=input()
    print(name + ", we are going to play a game . i am thinking of a number between 1 and 100")
    if(number%2==0):
        x='even'
    else:
        x='odd'
    print("this is an "+x+" number")
    time.sleep(.5)
    print("go ahead.guess!")
def pick():
    guessestaken=0
    while guessestaken<6:
        time.sleep(.25)
        enter=input("guess:")
        try:
            guess=int(enter)
            if guess<=100 and guess>=1:
                guessestaken=guessestaken+1
                if guessestaken<6:
                    if guess<number:
                        print("the guess is too low")
                    if guess>number:
                        print("guess is too high")
                    if guess !=number:
                        time.sleep(.5)
                        print("Try Again!")
                    if guess==number:
                       break
            if guess>100 or guess<1:
                print("number is not in range!")
                time.sleep(.25)
                print('please enter a number between 1 and 100')
        except:
            print("i don`t think that"+enter+" is a number .sorrry")
    if guess ==number:
                print('good job'+guessestaken+"guess")
    if guess!=number:
                print("the number was"+str(number))
playagain="Yes"
while playagain=="yes":
                intro()
                pick()
                print("do you want to play again?")
                playagain=input()
            