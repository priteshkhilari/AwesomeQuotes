import pandas as pd

data = {"emailID":[],
        "password" : [],
        "mID":[]}

df = pd.DataFrame(data)
df.to_csv("IDPass.csv")
