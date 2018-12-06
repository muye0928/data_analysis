"""we define unique repeat customers are the unique name in the specific period and their status are done"""
# import bookings data
import pandas as pd
df = pd.read_csv("bookings.csv")
df =df[df["Status"]=="done"]
index_month = pd.date_range('7/1/2017', periods=24, freq="M")
df["Full Name"] = df["First Name"]+ " " +df["Last Name"]
df = df[["Full Name","Appt Date"]]
df["Appt Date"] = pd.to_datetime(df["Appt Date"])

# find unique customers monthly
month = []
month_name = []
for i in index_month:
    month.append(i)
    tmp = df[(df["Appt Date"]<=i)&(df["Appt Date"]>i-1)]
    month_name.append(len(set(tmp["Full Name"])))
result = pd.DataFrame({"Month":month,"monthname":month_name})
result

# find unique customers weekly
index_week = pd.date_range('7/1/2017', periods=80, freq="W")
week = []
week_name = []
for i in index_week:
    week.append(i)
    tmp1 = df[(df["Appt Date"]<=i)&(df["Appt Date"]>i-1)]
    week_name.append(len(set(tmp1["Full Name"])))
result1 = pd.DataFrame({"week":week,"weekname":week_name})
result1

#find the repeat customers
first = df.drop_duplicates(subset = "Full Name",keep = "last")
first = first.reset_index()
df = df.reset_index()
# we find repeat customers using total booking data minus first time bookings
repeat = pd.concat([first,df]).drop_duplicates(keep = False)

#unique repeat customers weekly
repeat_week = []
repeatname = []
for i in index_week:
    repeat_week.append(i)
    tmp = repeat[(repeat["Appt Date"]<=i)&(repeat["Appt Date"]>i-1)]
    repeatname.append(len(set(tmp["Full Name"])))
result2 = pd.DataFrame({"week":repeat_week,"weekname":repeatname})
result2

#unique repeat customers monthly
repeat_month = []
repeatnamem = []
for i in index_month:
    repeat_month.append(i)
    tmp = repeat[(repeat["Appt Date"]<=i)&(df["Appt Date"]>i-1)]
    repeatnamem.append(len(set(tmp["Full Name"])))
result3 = pd.DataFrame({"week":repeat_month,"monthname":repeatnamem})
result3

