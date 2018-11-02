"""this task is to track how many people come back after using different codes monthly
and how many customers are new customers for the specific code """

import pandas as pd

df = pd.read_csv("bookings.csv")
df = df[["Appt Date", "Full Name", "Status", "Snailz Discount Code", "Full \nDiscounted", 'Id']]
df = df[df["Status"] == "done"]
df["Appt Date"] = pd.to_datetime(df["Appt Date"])
df.head()
df["year-month"] = df["Appt Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
df = df.sort_values("Appt Date")
df = df.reset_index()
df.head()
unique = df[df["Full \nDiscounted"] == True]
unique = unique.drop_duplicates("Id", "first")
first_time_visit = unique["index"].values
df["is_first_time"] = df.apply(lambda x: True if x["index"] in first_time_visit else False, axis=1)
repeat_visit = unique["Id"].values
df["is_repeat"] = df.apply(lambda x: True if x["Id"] in repeat_visit and x["is_first_time"] == False else False, axis=1)
year_month = df["year-month"].unique()
first_time_count = []
result_ym = []
repeat_count = []

for ym in year_month:
    result_ym.append(ym)
    tmp = df[df["year-month"] == ym]
    # fist_time_count
    first_time_count.append(len(tmp[tmp["is_first_time"] == True]))
    # repeat count
    repeat_count.append(len(tmp[tmp["is_repeat"] == True]))
result = pd.DataFrame({"year-month": result_ym, "unique": first_time_count, "repeat": repeat_count})
result

# for specific code: for example-- freemani
example = df[df["Snailz Discount Code"] == "freemani"]
example_unique = example.drop_duplicates("Id", "first")
df["first_ex"] = df.apply(lambda x: True if x["index"] in example_unique["index"].values else False, axis=1)
df["repeat_ex"] = df.apply(
    lambda x: True if x["Id"] in example_unique["Id"].values and x["first_ex"] == False else False, axis=1)

#example's result#
result_ym1 = []
first_time_count1 =[]
repeat_count1 =[]
for ym in year_month: # we defined year_month before
    result_ym1.append(ym)
    tmp = df[df["year-month"] == ym]
    # fist_time_count1
    first_time_count1.append(len(tmp[(tmp["first_web"] == True)]))
    # repeat count1
    repeat_count1.append(len(tmp[(tmp["repeat_web"] == True)]))
result1 = pd.DataFrame({"year-month": result_ym1, "unique": first_time_count1, "repeat": repeat_count1})
result1