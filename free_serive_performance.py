"""this task is to measure the free services performance, to find how many people came back and completed bookings
 and how many people came back no matter their bookings  status"""
import pandas as pd
df2 = pd.read_csv("bookings1125.csv")
df2["Date"] = df2["Appt Date"] +" " + df2["Start Time"]
df2["Date"] = pd.to_datetime(df2["Date"])
df2["year-month"] = df2["Date"].apply(lambda x: str(x.year) +"-"+ str(x.month))
df2 = df2[["Date","Full Name","Status","Full \nDiscounted"]]
##those are people who use the free services
full = df2[df2["Full \nDiscounted"] == True]
## drop the duplicated names for the one who used free services
name = full.drop_duplicates(subset="Full Name")
##use left join to get the result
result = pd.merge(df2,name[["Full Name", "year-month", "Date"]],on="Full Name", how='left')
# make sure the people used the free services first and then come back
result1 = result[result["Date_x"] > result["Date_y"]]
# get the monthly data
result1.groupby(['year-month_x']).size()

# to find out the how many completed bookings came from people who used the free services before
result2 = result1[result1["Status"] == "done"]
result2.groupby(['year-month_x']).size()