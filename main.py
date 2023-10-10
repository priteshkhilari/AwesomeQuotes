import sys
from login import *
from quotess import *
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
            mid = signin()
            if mid:
                print("Successfully signed in!")
                afterAuthentication(mid)
        elif var == 2:
            val = signup()
            if val:
                print("Successfully signed up!")


def afterAuthentication(mID):
    while True:
        val = int(input('''Press
    0. Sign Out
    1. All Quotes
    2. My Quotes
    3. My Favorite Quotes
    4. Like/Unlike Quote
    5. New Quote
    6. Edit Quote
    7. Delete Quote
    8. Change Password
    9. Edit Proﬁle'''))

        if val == 0:
            return
        elif val == 1:
            allquotes(mID)
        elif val == 2:
            myquotes(mID)
        elif val == 3:
            pass
        elif val == 4:
            pass
        elif val == 5:
            newquote(mID)
        elif val == 6:
            editmyQuote(mID)
            pass
        elif val == 7:
            deleteQuote(mID)
            pass
        elif val == 8:
            changePassword(mID)

















def terminate():
    print("Thanks for using Moderate Cya")
    sys.exit()




mainfunc()