import pandas as pd
import uuid
import re
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

        return None


# def signup1():
#     def passward(passs):
#         if len(passs) <8:
#             return False
#         alpha = False
#         numeric = False
#         special = False
#         for i in passs:
#             if i.isalpha():
#                 alpha = True
#             elif i.isnumeric():
#                 numeric = True
#             elif i in ["~","!","@","#","$","%","^","&","*","(",")","-","_","=","+","/","/","?",",","/",">","<",".",":",";"]:
#                 special = True
#         if alpha and numeric and special:
#             return True
#         else:
#             return False
#
#
#
#
#     while True:
#         val = int(input("Press 0 to exit\nPress any number to continue"))
#         if val == 0:
#             return False
#         email = input("Please enter email address here")
#         password = None
#         df = pd.read_csv("./IDPass.csv")
#         if email in list(df["emailID"]):
#             print("Email already exists")
#             continue
#         while True:
#             print("Password must be minimum 8 digits \nIt must contain alpha-numeric values \nAlong with special character ")
#             password = input("Please enter password here")
#             if passward(password):
#                 break
#         break
#     mid = uuid.uuid1()
#
#     new_df = pd.DataFrame({"emailID":email,"password":password,"mID":mid},index=[0])
#     df = pd.concat([df,new_df],ignore_index=True).set_index("mID")
#     df.to_csv("./IDPass.csv")
#
#     return True



def authenticate(email, password):
    df = pd.read_csv("./IDPass.csv")
    if email in list(df["emailID"]):
        lst = df.loc[df["emailID"] == email,["mID","password"]].values[0]
        mID = lst[0]
        password_db = str(lst[1])
        if password_db == password:
            return mID
        else:
            return None
    else:

        return None


def changePassword(mID):
    returned_mID = signin()
    if returned_mID ==None:
        return None
    ppattern = re.compile("(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$")
    if returned_mID == mID:
        df = pd.read_csv("./IDPass.csv")
        while True:
            new_password1 = input("Please enter new password")
            new_password2 = input("Please confirm new password")
            if new_password2 == new_password1:
                if ppattern.search(new_password2):
                    df.loc[df[df["mID"] == returned_mID].index, "password"] = new_password1

                    break
                else:
                    print("--Password must be minimum 8 digits \n--It must contain alpha-numeric values \n--Along with special character ")
                    val = input("Press 0 to abort & go to previous menu")
                    if val == "0":
                        return returned_mID
                    else:
                        continue

            else:
                print("Password doesnot matched please try again")
                val = input("Press 0 to abort & go to previous menu")
                if val == "0":
                    return returned_mID
                else:
                    continue

        df = df.set_index("mID")
        df.to_csv("./IDPass.csv")
        print("Password changed successfully")
        return returned_mID
    else:
        print("Authentication Failed")
        return None



def signup():
    df = pd.read_csv("./IDPass.csv")
    epattern = re.compile("^[a-z]+[0-9]*@[a-z]+\\.(com)|(net)|(in)|(org)$")
    ppattern = re.compile("(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$")
    ph_pattern = re.compile("^(0|\\+?91)?[0-9]{10}$")
    name = re.compile("^[A-Za-z-]+$")
    reg_email = None
    reg_password = None
    reg_phone = None
    reg_fname = None
    reg_lname = None
    mID = None
    while True:
        email = input("Please enter email address here")
        if email in list(df["emailID"]):
            print("Email already exists")
            continue
        else:
            if epattern.search(email):
                reg_email = email
                print("Email successfully registered")
                break
            else:
                print("Email address is invalid")
                val = input("Press 0 to exit")
                if val == "0":
                    return False
                continue
    while True:
        print("Password must be minimum 8 digits \nIt must contain alpha-numeric values \nAlong with special character ")
        password = input("Please enter password here")
        if ppattern.search(password):
            reg_password = password
            print("Password registered successfully")
            break
        else:
            continue

    while True:
        print("Phone number must be atleast 10 digits long")
        phone = input("Please enter phone number here")
        if ph_pattern.search(phone):
            reg_phone = phone
            print("Phone number successfully regestered")
            break
        else:
            print("Invalid phone number")
            val = input("Press 0 to exit")
            if val == "0":
                return False
            continue

    while True:
        fname = input("Please enter your first name here")
        lname = input("Please enter your last name here")
        if name.search(fname) and name.search(lname):
            reg_fname = fname
            reg_lname = lname
            break
        else:
            print("Invalid first name")
            val = input("Press 0 to exit")
            if val == "0":
                return False
            continue

    if reg_lname and reg_fname and reg_email and reg_password and reg_phone :
        mID = uuid.uuid1()

    data = {"mID":mID,"emailID":reg_email,"password":reg_password, "mobile":reg_phone,"f_name":reg_fname,"l_name":reg_lname}
    new_df = pd.DataFrame(data,index=[0])

    df = pd.concat([df, new_df], ignore_index=True).set_index("mID")
    df.to_csv("./IDPass.csv")
    return True




def editProfile(mID):
    df = pd.read_csv("./IDPass.csv")
    ph_pattern = re.compile("^(0|\\+?91)?[0-9]{10}$")
    name = re.compile("^[A-Za-z-]+$")

    def changef_name(mID):
        reg_fname = None
        while True:
            fname = input("Please enter your first name here")
            if name.search(fname) :
                reg_fname = fname
                break
            else:
                print("Invalid first name")
                val = input("Press 0 to exit")
                if val == "0":
                    return False
                continue
        condition = df["mID"] == mID
        df.loc[condition,"f_name"] = reg_fname
        df.set_index("mID",inplace=True)
        df.to_csv("./IDPass.csv")
        return True

    def changel_name(mID):
        reg_lname = None
        while True:
            lname = input("Please enter your first name here")
            if name.search(lname):
                reg_lname = lname
                break
            else:
                print("Invalid Last name")
                val = input("Press 0 to exit")
                if val == "0":
                    return False
                continue
        condition = df["mID"] == mID
        df.loc[condition, "l_name"] = reg_lname
        df.set_index("mID",inplace=True)
        df.to_csv("./IDPass.csv")
        return True

    def changemobile(mID):
        reg_mobile = None
        while True:
            mobile = input("Please enter your mobile number here")
            if ph_pattern.search(mobile):
                reg_mobile = mobile
                break
            else:
                print("Invalid number")
                val = input("Press 0 to exit")
                if val == "0":
                    return False
                continue
        condition = df["mID"] == mID
        df.loc[condition, "l_name"] = reg_mobile
        df.set_index("mID",inplace=True)
        df.to_csv("./IDPass.csv")
        return True



    returned_mID = signin()
    if returned_mID == None:
        return  None
    if returned_mID == mID:
        val = input("Press 1 to change f_name\nPress 2 to change l_name\nPress 3 to change mobile number")
        if val in ["1","2","3"]:
            if val == "1":
                if changef_name(mID):
                    print("Successfully edited")
                    return returned_mID
            elif val == "2":
                if changel_name(mID):
                    print("Successfully edited")
                    return returned_mID
            elif val == "3":
                if changemobile(mID):
                    print("Successfully edited")
                    return returned_mID
        else:
                print("Invalid choice")
                return returned_mID
    else:
        print("Authentication failed")
        return None




def mydetails(mID):
    df = pd.read_csv("./IDPass.csv")
    condition = df["mID"] == mID
    new_df = df.loc[condition,["f_name","l_name","mobile"]]
    print(new_df)
