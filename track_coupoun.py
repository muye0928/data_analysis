"""this task is to track how many people come back after using different codes monthly
and how many customers are new customers for the specific code """

import pandas as pd
df = pd.read_csv("bookings.csv")

def preprocess(df):
    df = df[df["Status"] == "done"]
    df["Date"] = df["Appt Date"] +" "+ df["Start Time"]
    df["Date"] = pd.to_datetime(df["Date"])
    df = df[["Date", "Full Name","Snailz Discount Code"]]
    df = df.sort_values("Date")
    df = df.reset_index()
    df["Snailz Discount Code"] = df["Snailz Discount Code"].str.strip()
    df["Snailz Discount Code"] = df["Snailz Discount Code"].str.lower()
    df["year-month"] = df["Date"].apply(lambda x: str(x.year) +"-"+ str(x.month))
    return df
df = preprocess(df)

#onemonth
# how many people came back based on one month (unique)
code = "spring10"
tmp = df[df["Snailz Discount Code"] ==code]
current = df[df["year-month"] =="2018-11"]
result = pd.merge(current,tmp[["Full Name", "year-month", "Date"]],on="Full Name", how='left')
df1 = result[result["year-month_x"] == result["year-month_y"]]
df1 = df1[df1["Date_x"] > df1["Date_y"]]
len(set(df1["Full Name"]))

#two month
# how many people came back based on this month and pevious month (unique)
code = "spring10"
tmp = df[df["Snailz Discount Code"] ==code]
i="2018-8"
current = df[df["year-month"]==i]
two = tmp[(tmp["Date"]<="2018/8/31")&(tmp["Date"]>="2018/7/1")]
result1 = pd.merge(current,two[["Full Name", "year-month", "Date"]],on="Full Name", how='left')
df2 = result1[result1["year-month_x"] == i]
df2 = df2[df2["Date_x"] > df2["Date_y"]]
len(set(df2["Full Name"]))
