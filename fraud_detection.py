import pandas as pd
#load data
df = pd.read_csv("bookings.csv")
# make sure their status are done and they used free services code
df = df[df["Status"] =="done"]
df = df[df["Free"] == True]
# except other columns in original dataframe
df = df[["Full Name","Snailz Discount Code","Appt Date"]]
# find the duplicated names and sort by name
name = df["Full Name"]
result = df[name.isin(name[name.duplicated()])].sort_values(by=['Full Name'])
result.to_csv("fraud.csv")