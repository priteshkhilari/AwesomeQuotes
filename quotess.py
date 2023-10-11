import pandas as pd
import uuid
def allquotes(mID):
    if mID:
        quotes_df = pd.read_csv("./quotes.csv",index_col=False)
        aq_df = quotes_df[["author","text"]].set_index("author")
        print(aq_df)
        return

def myquotes(mID):
    if mID:
        quotes_df = pd.read_csv("./quotes.csv",index_col=False)
        print(quotes_df[quotes_df["mID"] == mID][["author","text"]].set_index("author"))
        return



def newquote(mID):

    if mID:
        quotes_df = pd.read_csv("./quotes.csv",index_col=0)
        newqte = input("Please enter quote here")
        author = input("Please enter name of author here")
        quid = uuid.uuid1()
        data = { "Qid":quid,
                "text":newqte,
                "author":author,
                "mID":mID
                }
        df = pd.DataFrame(data,index=[0])
        quotes_df = pd.concat([quotes_df,df],ignore_index=True)
        quotes_df.to_csv("./quotes.csv")
        return



def deleteQuote(mID):
    if mID:
        quotes_df = pd.read_csv("./quotes.csv",index_col=0)
        # print(quotes_df)
        my_quotesdf = quotes_df[quotes_df["mID"] == mID].reset_index().set_index("index")
        if len(my_quotesdf) == 0:
            print("You can delete quotes added by you! No more quotes to delete")
            return
        print(my_quotesdf[["text","author"]])
        val = input("Please enter index number which you wanna delete")
        if val.isdigit():
            val = int(val)
        else:
            print("Invalid Choice")
            return
        if val in my_quotesdf.index.tolist():
            mylist = quotes_df.iloc[[val]].values[0]
            # print(mylist)
            qid = mylist[0]
            if mID == mylist[3]:
                mask = ~((quotes_df["mID"] == mID) & (quotes_df["Qid"] ==qid))
                quotes_df = quotes_df[mask]
                quotes_df.to_csv("./quotes.csv")
                print("Successfully deleted")
        else:
            print("Please enter valid index")
            return






def editmyQuote(mID):
    quotes_df = pd.read_csv("./quotes.csv", index_col=0)
    # print(quotes_df)
    my_quotesdf = quotes_df[quotes_df["mID"] == mID].reset_index().set_index("index")
    if len(my_quotesdf) == 0:
        print("You can edit quotes added by you! No more quotes to Edit")
        return
    print(my_quotesdf[["text", "author"]])
    val = input("Please enter index number which you wanna edit")
    if val.isdigit():
        val = int(val)
    else:
        print("Invalid Choice")
        return
    if val in my_quotesdf.index.tolist():
        mylist = quotes_df.loc[val].tolist()
        # .values[0]
        # print(mylist)
        qid = mylist[0]
        if mID == mylist[3]:
            newqte = input("Please enter quote here")
            author  = input("Please enter author here")
            condition = (quotes_df["mID"] == mID) & (quotes_df['Qid'] == qid)
            quotes_df.loc[condition,"author"] = author
            quotes_df.loc[condition, "text"] = newqte
            quotes_df.to_csv("./quotes.csv")
            print("Successfully Edited")
        else:
            print("Something went wrong")
    else:
        print("Please enter valid index")
        return







def likeQuote(mID):
    fq = pd.read_csv("./favouriteQuotes.csv",index_col=0)
    quotes_df = pd.read_csv("./quotes.csv", index_col=0)
    mask = ~(quotes_df["mID"] == mID)
    x = myfavourite_quote(mID)
    series = x["Qid"]
    mask2 = ~(quotes_df["Qid"].isin(series))
    condition = (mask)& (mask2)
    canlike = quotes_df[condition].reset_index().set_index("index")
    if len(canlike) == 0:
        print("You have all caught up! No more quotes to like")
        return
    print(canlike[["author" , "text"]])
    val = input("Please enter index number which you wanna like")

    if val.isdigit():
        val = int(val)
    else:
        print("Invalid Choice")
        return

    if val in canlike.index.tolist():
        qid = canlike.loc[val,"Qid"]
        data = {"mID": mID,
                "Qid": qid}
        new_liked = pd.DataFrame(data,index=[0])
        fq = pd.concat([fq,new_liked],ignore_index=True)
        fq.to_csv("./favouriteQuotes.csv")
        print("Successfully Liked")
        return
    else:
        print("Please enter valid index")
        return




def myfavourite_quote(mID):
    fq = pd.read_csv("./favouriteQuotes.csv", index_col=0)
    quotes_df = pd.read_csv("./quotes.csv", index_col=0)
    my_liked = fq[fq["mID"] == mID]["Qid"]
    new_df = quotes_df[quotes_df["Qid"].isin(my_liked)]
    return new_df


def unlikeQuote(mID):
    df = myfavourite_quote(mID)
    # print(df)
    new_df = df[df["mID"] != mID].reset_index().set_index("index")
    if len(new_df) == 0:
        print("You have all caught up! No more quotes to unlike")
        return
    print(new_df[["author" , "text"]])
    val = input("Please enter index number which you wanna unlike")

    if val.isdigit():
        val = int(val)
    else:
        print("Invalid Choice")
        return

    index_list = new_df.index.tolist()
    if val in index_list:
        qid = new_df.loc[val,"Qid"]
        fq = pd.read_csv("./favouriteQuotes.csv", index_col=0)
        mask = ~((fq["mID"] == mID) & (fq["Qid"]==qid))
        fq = fq[mask]
        fq.to_csv("./favouriteQuotes.csv")
        print("Successfully Uniked")
        return
    else:
        print("Please enter valid index")
        return