"""this task is to count how many customers came from each channel monthly/weekly and 
how many bookings came from each channel monthly/weekly"""
# import registration data
import pandas as pd
df = pd.read_csv("registration.csv")
df = df[["Date", "full name", "Source"]]
df["Date"] = pd.to_datetime(df["Date"])
df["year-month"] = df["Date"].apply(lambda x: str(x.year) +"-"+ str(x.month))

# data cleaning for source text data
origin = df["Source"].values
df["Source"] = [i.replace(" ", "").lower() if type(i) == str else None for i in origin]
df = df.dropna()
df = df[~df['Source'].isin(["x"])]
df = df[~df['Source'].isin(["ad"])]
df = df.replace("fb", "facebook")
df = df.replace("ig","instagram")
df['Source'] = df['Source'].str.replace('[^\w\s]','')
df=df[~df['Source'].isin(["no"])]

def normalize(lst, origin, target):
    for word in lst:
        if word in origin:
            return target
    return origin

apple = lambda x: normalize(["app"], x, "apple")
ins = lambda x: normalize(["ins", "gram", "ig"], x, "instagram")
friend = lambda x: normalize(["rf","friend","refer","daughter","cousin","family","sister","wife","husband","gf","told","coworker","fried","roommate"],x,"friend")
yelp = lambda x: normalize(["yel","review"],x,"yelp")
website = lambda x: normalize(["web","online","search","snailz","internet"],x,"website")
salon = lambda x: normalize(["sal","nail","street","walk","sign","flyer","shop","window"],x,"salon")
google = lambda x: normalize(["goog"],x,"google")
pinterest = lambda x :normalize(["pint"],x,"pinterest")
event = lambda x: normalize(["event","cew","wework"],x,"event")
fb = lambda x: normalize(["fb","face","book","social"],x,"facebook")

df['Source'] = list(map(ins,df['Source'] ))
df['Source'] = list(map(fb,df['Source'] ))
df['Source'] = list(map(friend,df['Source'] ))
df['Source'] = list(map(apple,df['Source'] ))
df['Source'] = list(map(yelp,df['Source'] ))
df['Source'] = list(map(website,df['Source'] ))
df['Source'] = list(map(salon,df['Source'] ))
df['Source'] = list(map(google,df['Source'] ))
df['Source'] = list(map(pinterest,df['Source'] ))
df['Source'] = list(map(event,df['Source'] ))

#load booking data
df2 = pd.read_csv("bookings1126.csv")
df2 = df2[["Full Name","Appt Date",'Referral Code','Snailz Discount Code',"Status"]]
df2["Appt Date"] = pd.to_datetime(df2["Appt Date"])
df2 = df2[df2["Status"] == "done"]
df2["year-month"] = df2["Appt Date"].apply(lambda x: str(x.year) +"-"+ str(x.month))

# added people use webcode into the source of website
webcode = df2[df2["Snailz Discount Code"] =="web10"].drop_duplicates(subset = "Full Name")
source_web = df[df["Source"] == "website"]
webname = webcode["Full Name"]. append(source_web["full name"])
webname = set(webname)

# added people who use the refer code into the source of friend
refer = df2.dropna(subset = ["Referral Code"])
source_friend = df[df["Source"] == "friend"]
refername = refer["Full Name"].append(source_friend["full name"])
refername = set(refername)

#count monthly registration data from different channels
sour_fb = df[df["Source"] == "facebook"]
refb = sour_fb[["full name", "year-month"]]
refb.columns = ["full name", "ym"]
refb = refb.groupby("ym").count()
refb

#count weekly registration data
df['Week/Year'] = df['Date'].apply(lambda x: "%d/%d" % (x.week, x.year))
sour_fb = df[df["Source"] == "facebook"]
refb = sour_fb[["full name", "Week/Year"]]
refb.columns = ["full name", "ym"]
refb = refb.groupby("ym").count()
refb

# booking data from different channels monthly
from collections import defaultdict

data = defaultdict(list)

index_month = pd.date_range('7/1/2017', periods=24, freq="M")

channel = ["instagram", "google", "yelp", "twitter", "facebook", "pinterest", "apple", "friend", "salon", "website",
           "event"]
for c in channel:
    for i in index_month:
        tmp = df2[(df2["Appt Date"] <= i + 1) & (df2["Appt Date"] > i)]
        data[c].append(len(tmp[(tmp[c] == True)]))

pd.DataFrame.from_dict(data)

# booking data from different channel weekly
# weekly
from collections import defaultdict

data_week = defaultdict(list)

index_week = pd.date_range('7/1/2017', periods=80, freq="W")

channel = ["instagram", "google", "yelp", "twitter", "facebook", "pinterest", "apple", "friend", "salon", "website",
           "event"]
for c in channel:
    for i in index_week:
        tmp = df2[(df2["Appt Date"] <= i + 1) & (df2["Appt Date"] > i)]
        data_week[c].append(len(tmp[(tmp[c] == True)]))
