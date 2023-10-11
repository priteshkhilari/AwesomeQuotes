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
        val = input('''Press
    0. Sign Out
    1. All Quotes
    2. My Quotes
    3. My Favorite Quotes
    4. Like/Unlike Quote
    5. New Quote
    6. Edit Quote
    7. Delete Quote
    8. Change Password
    9. Edit Proﬁle
    10. View my Details''')
        if val.isdigit():
            val = int(val)
        else:
            continue

        if val == 0:
            mID = None
            return mID
        elif val == 1:
            allquotes(mID)
        elif val == 2:
            myquotes(mID)
        elif val == 3:
            x = myfavourite_quote(mID)
            print(x[["author" , "text"]])
            pass
        elif val == 4:
            newval   = int(input("Press 1 to like a quote\n Press 2 to unlike"))
            if newval == 1:
                likeQuote(mID)
            elif newval == 2:
                unlikeQuote(mID)
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
            mID = changePassword(mID)
            if mID == None:
                return
        elif val == 9:
            mID = editProfile(mID)
            if mID == None:
                return
        elif val == 10:
            mydetails(mID)

















def terminate():
    print("Thanks for using Moderate Cya")
    sys.exit()




mainfunc()