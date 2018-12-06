import pandas as pd
df2 = pd.read_csv("bookings1206.csv")
df2["Full Name"] = df2["First Name"]+ " " +df2["Last Name"]
df2["Appt Date"] = pd.to_datetime(df2["Appt Date"])
df2 = df2[df2["Status"]=="done"]
df2 = df2[["Appt Date","GROSS","Full Name"]]
index = pd.date_range("7/1/2017",periods=79,freq="W")
#aveage customer spending weekly(to add each customers total spending and then find the average of each customers)
a = []
week = []
for i in index:
    week.append(i)
    tmp = df2[(df2["Appt Date"]<= i)&(df2["Appt Date"]> i-1)]
    group = tmp.groupby(["Full Name","Appt Date"]).sum()
    group = group.mean().values[0]
    a.append(group)
result =pd.DataFrame({"week":week,"spending":a})
result

#aveage customer spending monthly
df2["year-month"] = df2["Date"].apply(lambda x: str(x.year) +"-"+ str(x.month))
DF2 = df2.groupby(['year-month','Full Name']).sum()
DF2.groupby("year-month").mean()