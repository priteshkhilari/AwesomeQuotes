import pandas as pd
import uuid
def allquotes(mID):
    if mID:
        quotes_df = pd.read_csv("./quotes.csv")
        aq_df = quotes_df[["author","text"]].set_index("author")
        print(aq_df)
        return

def myquotes(mID):
    if mID:
        quotes_df = pd.read_csv("./quotes.csv")
        print(quotes_df[quotes_df["mID"] == mID][["author","text"]])
        return



def newquote(mID):

    if mID:
        quotes_df = pd.read_csv("./quotes.csv")
        newqte = input("Please enter quote here")
        author = input("Please enter name of author here")
        quid = uuid.uuid1()
        data = {"Qid":quid,
                "text":newqte,
                "author":author,
                "mID":mID}
        df = pd.DataFrame(data,index=[0])
        quotes_df = pd.concat([quotes_df,df],ignore_index=True).set_index("Qid")
        quotes_df.to_csv("./quotes.csv")
        return



def deleteQuote(mID):
    if mID:
        quotes_df = pd.read_csv("./quotes.csv")
        my_quotesdf = quotes_df[quotes_df["mID"] == mID]
        print(my_quotesdf[["author", "text"]])
        val = input("Please enter index number which you wanna delete")






def editmyQuote(mID):
    pass