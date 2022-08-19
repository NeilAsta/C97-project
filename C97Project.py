
takenchances=0

import random
number=random.randint(0,10)
#print(number)


while(takenchances<5):
    takenchances+=1
    guess=int(input("please guess a number between 0 and 10 "))
    if (guess==number):
        print ("Wow! you got it with "  "chances left.")
    elif (guess>number):
        print("Ooh too high")
    elif (guess<number):
        print("Ooh too low")
    
      