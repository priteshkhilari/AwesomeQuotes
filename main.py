import sys
from login import *
def mainfunc():


    flag = False
    while True:
        var = int(input('''Welcome to Moderate
      Press
      0 . To Exit
      1 . Sign in
      2 . Sign up\n'''))

        if var == 0:
              terminate()
        elif var == 1:
            flag , mid = signin()
        elif var == 2:
            val = signup()
            if val:
                print("Successufully signed up!")


def afterAuthentication():
    pass


def terminate():
    print("Thanks for using Moderate Cya")
    sys.exit()




mainfunc()