import random
playing=True
number=random.randint(10,40)

print("i will generate a random number from 10 to 40 and you have to guess it")

while playing:
    guess=int(input)