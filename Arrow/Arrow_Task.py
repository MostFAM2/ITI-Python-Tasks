#--------------------------------------------------------------------------
# @File			:	Arrow_Task.py
# @Author		:	Mostafa Mahmoud 
# @Brief		:	Program To Print Arrow in 4 Direction 
#--------------------------------------------------------------------------
import os
import time

NumOfStars = int(input("Enter Number of Stars To Form The Arrow Head :  "))

while True:
    
    os.system('cls')
    
    ''' -------- [Right Arrow] -------- '''
    for i in range(((NumOfStars*2)+1)):
        print()
    for i in range(NumOfStars):
        if i == (NumOfStars-1):
            print(" "*((NumOfStars*6)-1),end="");
            print("* "*(2*NumOfStars),end="");
            print("* "*(i+1))
        else:
            print(" "*((NumOfStars*6)-1),end="");
            print("  "*(2*NumOfStars),end="")
            print((i+1)*"* ")
    for j in range(NumOfStars-1,0,-1):
        print(" "*((NumOfStars*6)-1),end="");
        print("  "*(2*NumOfStars),end="")
        print((j)*"* ")
    ''' ===================================== '''

    time.sleep(1)
    os.system('cls')

    ''' -------- [Down Arrow] -------- '''
    for i in range(NumOfStars*3):
        print()
    for i in range(0,NumOfStars*2,1):
        print(" "*(NumOfStars*5),end="")
        print(" "*(NumOfStars-1),end="")
        print("*")
    for i in range(NumOfStars):
        print((NumOfStars*5)*" ",end="");
        for j in range(i):
            print(" ",end="")
        for j in range(i,NumOfStars-1):
            print("*",end="")
        for j in range(i,NumOfStars):
            print("*",end="")
        print()
    ''' ===================================== '''

    time.sleep(1)
    os.system('cls')

    ''' -------- [Left Arrow] -------- '''
    for i in range(((NumOfStars*2)+1)):
        print()
    for i in range(NumOfStars):
        if i== (NumOfStars-1):
            print(" *"*(2*NumOfStars),end="");
            print(" *"*(i+1))
        else:
            print("  "*(NumOfStars-i-1),end="")
            print((i+1)*" *")
    for j in range(1,NumOfStars,1):
        print("  ",end="")
        print((NumOfStars-j)*" *")
        print((j)*"  ",end="")
    ''' ===================================== '''

    time.sleep(1)
    os.system('cls')

    ''' -------- [UP Arrow] -------- '''
    print()
    for i in range(NumOfStars):
        print(" "*(NumOfStars*5),end="")
        for j in range(i+1,NumOfStars):
            print(" ",end="")
        for j in range(i):
            print("*",end="")
        for j in range(i+1):
            print("*",end="")
        print()
    for i in range(0,NumOfStars*2,1):
        print(" "*(NumOfStars*5),end="")
        print(" "*(NumOfStars-1),end="")
        print("*")
    time.sleep(1)
    ''' ===================================== '''
