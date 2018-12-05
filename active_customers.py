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

index_month = pd.date_range('1/1/2017',periods = 24, freq = "M")
def intersection(lst1, lst2): 
    return list(set(lst1) & set(lst2))
book_month =[]
month_record =[]
for ym in index_month:
    month_record.append(ym)
    monthdata = result[result["Date"] <= ym]
    bookmonth = df2[df2['Date']<=ym]
    #bookmonth data count
    book_month.append(len(intersection(bookmonth["Full Name"],monthdata["full name"])))
result_ym =pd.DataFrame({"month": month_record,"book":book_month})
result_ym

index_week = pd.date_range('7/1/2017',periods = 79, freq = "W")
book_week =[]
week_record =[]
for i in index_week:
    week_record.append(i)
    weekdata = result1[result1["Date"] <= i]
    bookweek = df2[df2['Date']<=i]
    #bookmonth data count
    book_week.append(len(intersection(bookweek["Full Name"],weekdata["full name"])))
result_week =pd.DataFrame({"week": week_record,"book":book_week})
result_week
