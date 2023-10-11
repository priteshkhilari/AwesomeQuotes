import pandas as pd
import uuid
def signin():
    email = input("Please enter your email id here")
    password = input("Please enter your password here")
    moderateID = authenticate(email,password)
    if moderateID:
        return moderateID
    else:
        print("------------------------------")
        print("| Invalid UserID or Password |")
        print("------------------------------")
        return False


def signup():
    def passward(passs):
        if len(passs) <8:
            return False
        alpha = False
        numeric = False
        special = False
        for i in passs:
            if i.isalpha():
                alpha = True
            elif i.isnumeric():
                numeric = True
            elif i in ["~","!","@","#","$","%","^","&","*","(",")","-","_","=","+","/","/","?",",","/",">","<",".",":",";"]:
                special = True
        if alpha and numeric and special:
            return True
        else:
            return False




    while True:
        val = int(input("Press 0 to exit\nPress any number to continue"))
        if val == 0:
            return False
        email = input("Please enter email address here")
        password = None
        df = pd.read_csv("./IDPass.csv")
        if email in list(df["emailID"]):
            print("Email already exists")
            continue
        while True:
            print("Password must be minimum 8 digits \nIt must contain alpha-numeric values \nAlong with special character ")
            password = input("Please enter password here")
            if passward(password):
                break
        break
    mid = uuid.uuid1()

    new_df = pd.DataFrame({"emailID":email,"password":password,"mID":mid},index=[0])
    df = pd.concat([df,new_df],ignore_index=True).set_index("mID")
    df.to_csv("./IDPass.csv")

    return True



def authenticate(email, password):
    df = pd.read_csv("./IDPass.csv")
    lst = df.loc[df["emailID"] == email,["mID","password"]].values[0]
    # print(lst)
    mID = lst[0]
    password_db = lst[1]
    if password_db == password:
        return mID
    else:
        return False


def changePassword(mID):
    passw = input("please authenticate yourself\nPlease enter password here")
    df = pd.read_csv("./IDPass.csv")
    email = df.loc[df["mID"] ==mID,"emailID" ].values[0]

    mid = authenticate(email,passw)
    if mid == mID:
        while True:
            new_password1 = input("Please enter new password")
            new_password2 = input("Please confirm new password")
            if new_password2 == new_password1:
                df.loc[df[df["mID"] == mid].index, "password"] = new_password1
                break
            else:
                print("Password doesnot matched please try again")
                continue
        df = df.set_index("mID")
        df.to_csv("./IDPass.csv")
        return



