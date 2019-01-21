"""this task is to measure the free services performance, to find how many people came back and completed bookings
 and how many people came back no matter their bookings  status"""
import pandas as pd


df = pd.read_csv("bookings0113.csv")
df = df[["Full Name","Free","Appt Date","Start Time","Status"]]
df["Date"] = df["Appt Date"]+" "+df["Start Time"]
df["Appt Date"] = pd.to_datetime(df["Appt Date"])
df["Date"]= pd.to_datetime(df["Date"])
free = df[df["Free"]==True]

##those are people who use the free services
week1 = free[(free["Appt Date"]>="2019/01/07")&(free["Appt Date"]<="2019/01/13")]
len(set(week1["Full Name"])) # unique name

# all status 
result = pd.merge(df,free[["Full Name", "Date"]],on="Full Name", how='left')
# make sure the people used the free services first and then come back
result1 = result[result["Date_x"] > result["Date_y"]]

# how many bookings came from those who used free services
week = result1[(result1["Appt Date"]>="2019/01/07")&(result1["Appt Date"]<="2019/01/13")]
len(week)

# how many completed bookings came from those used free services
week_done = week[week["Status"]=="done"]
len(week_done)
