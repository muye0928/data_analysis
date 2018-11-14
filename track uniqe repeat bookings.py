"""this task is to track how many people come back(cumulative repeat bookings) after using different codes monthly
and how many people came back based on 2-month code-users and how many people came back based on this month code-users
 """


#for cumulative repeat bookings
import pandas as pd
df = pd.read_csv("bookings1114.csv")
code = "web10"
def preprocess(df):
    df = df[["appt", "Full Name", "Status", "Snailz Discount Code"]]
    df = df[df["Status"] == "done"]
    df["appt"] = pd.to_datetime(df["appt"])
    df["year-month"] = df["appt"].apply(lambda x: str(x.year) +"-"+ str(x.month))
    df = df.sort_values("appt")
    df = df.reset_index()
    origin_code = df["Snailz Discount Code"].values
    df["Snailz Discount Code"] = [i.replace(" ", "").lower() if type(i) == str else None for i in origin_code]
    return df
df = preprocess(df)
df.head()

web = df[df["Snailz Discount Code"] == code]
result = pd.merge(df,web[["Full Name", "year-month", "appt"]],on="Full Name", how='left')
df1 = result[result["appt_x"] > result["appt_y"]]

df2 = df1[["Full Name", "year-month_x"]]
df2.columns = ["Full Name", "ym"]
df2 = df2.drop_duplicates() # to make sure there are unique customers
result = df2.groupby("ym").count()
result

###for one-month based repeat bookings
web = df[df["Snailz Discount Code"] == code]
first = web[web["year-month"] == "2018-9"]
result = pd.merge(df,first[["Full Name", "year-month", "appt"]],on="Full Name", how='left')
df3 = result[result["year-month_x"] == result["year-month_y"]]
df3 = df3[df3["appt_x"] > df3["appt_y"]]

df4 = df3[["Full Name", "year-month_x"]]
df4.columns = ["Full Name", "ym"]
df4 = df4.drop_duplicates()
df4 = df4.groupby("ym").count()
df4

###for two-month based repeat bookings
i="2018-8"
web = df[df["Snailz Discount Code"] == code]
first = web[web["year-month"] == i]
two = web[web["year-month"] == "2018-7"]
time = first.append(two)
result = pd.merge(df,time[["Full Name", "year-month", "appt"]],on="Full Name", how='left')
df5 = result[result["year-month_x"] == i]
df5 = df5[df5["appt_x"] > df5["appt_y"]]

df6 = df5[["Full Name", "year-month_x"]]
df6.columns = ["Full Name", "ym"]
df6 = df2.drop_duplicates()
df6 = df3.groupby("ym").count()
df6