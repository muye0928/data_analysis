"""" we define active customers are those in registration tab and still subscribed and at least completed bookings once"""
# load data
import pandas as pd
df1 = pd.read_csv("registration.csv")
df2 = pd.read_csv("bookings.csv")
df3 = pd.read_csv("subscribed.csv")

result =pd.merge(df1, df3, left_on="Email", right_on="Email Address", how="inner")
result = result[["Date","Email","full name"]]
# this result are unique customers who subscribed and registered and the day until oct02
result = result.drop_duplicates(subset = "Email")
result.head()

# data cleaning for bookings dat, create a column to show month-year and make sure those data are completed bookings
df2["Date"] = df2["Appt Date"] +" " + df2["Start Time"]
df2["Date"] = pd.to_datetime(df2["Date"])
df2["year-month"] = df2["Date"].apply(lambda x: str(x.year) +"-"+ str(x.month))
df2 = df2[["Full Name","Date","Status","year-month"]]
df2 = df2[df2["Status"] == "done"]

#total active and registration customer until this month
from datetime import datetime
result["Date"]=pd.to_datetime(result["Date"])
month = result[result["Date"]<datetime(2018,10,1,0,0)]

# book data until this month
bookmonth = df2[df2["Date"] < datetime(2018, 10, 1, 0, 0)]
#drop duplicate names
bookmonth = bookmonth.drop_duplicates(subset = "Full Name")

# The number of True are the number we want
bookmonth["Full Name"].isin(month["full name"]).value_counts()