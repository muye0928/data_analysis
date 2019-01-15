import pandas as pd
df = pd.read_csv("bookings.csv")
df = df[["Status","Snailz Discount Code","Appt Date","Full Name"]]
df = df[df["Status"] == "done"]
df["Snailz Discount Code"] = [i.replace(" ", "").lower() if type(i) == str else None for i in df["Snailz Discount Code"]]
df["Appt Date"] = pd.to_datetime(df["Appt Date"])

# unique completed bookings (first time only )
web = df[df["Snailz Discount Code"] == "web10"]
dec = web[(web["Appt Date"] >="2018/11/1")& (web["Appt Date"] <="2018/12/31")] # customized booking time
len(set(dec["Full Name"]))

# cumulative repeat bookings
result = pd.merge(df,web[["Full Name", "Appt Date","Snailz Discount Code"]],on="Full Name", how='left')
result = result[result["Appt Date_x"] > result["Appt Date_y"]]
len(set(result["Full Name"]))

# repeat bookings using this code in the customized time
repeat_dec = result[(result["Appt Date_x"]>="2018/12/1")&(result["Appt Date_x"]<="2018/12/31")]
len(set(repeat_dec["Full Name"]))


#in this way, we could count the number in flexiable time. It become easily to count repeat bookings based on
# one-month and two-month first booking data.