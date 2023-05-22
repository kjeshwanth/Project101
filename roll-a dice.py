import random
roll=input("do you want to roll a dice")

min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y": 
    no=random.randint(1,6)
    print ("Rolling dice...")
    print ("The value is....")
    print (random.randint(min,max))

    roll_again = input("Roll the dice again?")