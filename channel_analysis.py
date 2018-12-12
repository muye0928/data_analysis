"""this task is to count how many customers came from each channel monthly/weekly and 
how many bookings came from each channel monthly/weekly"""
# import registration data
import pandas as pd
df = pd.read_csv("registration.csv")
df = df[["Date", "full name", "Source"]]
df["Date"] = pd.to_datetime(df["Date"])

# data cleaning for source text data
origin = df["Source"].values
df["Source"] = [i.replace(" ", "").lower() if type(i) == str else None for i in origin]
df = df.replace("fb", "facebook")
df = df.replace("ig","instagram")
df['Source'] = df['Source'].str.replace('[^\w\s]','')
df = df[~df['Source'].isin(["no"])]
df["Source"].fillna("No Source", inplace = True) 

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
df = df[~df['Source'].isin(["ad"])]

#load booking data
df2 = pd.read_csv("bookings.csv")
df2["Full Name"] = df2["First Name"] +" " +df2["Last Name"]
df2 = df2[["Full Name","Appt Date",'Referral Code','Snailz Discount Code',"Status"]]
df2["Appt Date"] = pd.to_datetime(df2["Appt Date"])
df2 = df2[df2["Status"] == "done"]

# added people use webcode into the source of website
webcode = df2[df2["Snailz Discount Code"] =="web10"]
webname = set(webcode["Full Name"])
df["Source"] = df.apply(lambda x: "website" if x["full name"] in webname and x["Source"] == "No Source" else x["Source"],axis= 1)

# added people who use the refer code into the source of friend
refer = df2.dropna(subset = ["Referral Code"])
refername = set(refer["Full Name"])
df["Source"] = df.apply(lambda x: "friend" if x["full name"] in refername and x["Source"] =="No Source" else x["Source"],axis= 1)

#count monthly registration data from different channels
index_month = pd.date_range('7/1/2017',periods = 24, freq = "M")
from collections import defaultdict
data = defaultdict(list)
channel = ["instagram", "google","yelp","twitter","facebook","pinterest","apple","friend","salon","website","event"]
for c in channel:
    for i in index_month:
        tmp = df[(df["Date"] <= i) &(df["Date"] >i-1)]
        data[c].append(len(tmp[(tmp["Source"] == c)]))
pd.DataFrame.from_dict(data)

#registration weekly
index_week = pd.date_range('7/1/2017',periods = 75, freq = "W")
from collections import defaultdict
data = defaultdict(list)
channel = ["instagram", "google","yelp","twitter","facebook","pinterest","apple","friend","salon","website","event"]
for c in channel:
    for i in index_week:
        tmp = df[(df["Date"] <= i) &(df["Date"] >i-1)]
        data[c].append(len(tmp[(tmp["Source"] == c)]))
abc = pd.DataFrame.from_dict(data)

# to determine each bookings' source
df2.loc[:,'source'] = 'yyy'
source = ["instagram", "google","yelp","facebook","apple","salon","pinterest","event","twitter","website","friend"]
for item in source:
    source_a = df[df["Source"] == item]
    tmp = set(source_a["full name"])
    df2["source"] = df2.apply(lambda x: item if x["Full Name"] in tmp else x["source"],axis=1)

# who used referral code and his/ her source cannot classificated in previous channels
df2["Referral Code"].fillna("no", inplace = True)
df2["source"] = df2.apply(lambda x: "friend" if x["Referral Code"]!="no" and x["source"] =="yyy" else x["source"],axis =1)
    
# bookings' source data monthly 
index_month = pd.date_range('7/1/2017',periods = 24, freq = "M")
container = list()
for i in index_month:
    tmp = df2[(df2["Appt Date"] <= i) &(df2["Appt Date"] >i-1)]
    container.append(tmp["source"].value_counts().to_frame(i.strftime("%Y-%m"))) 
result = pd.concat(container, axis=1).fillna(0)

#bookings'source data weekly
index_week = pd.date_range('7/1/2017',periods = 80, freq = "W")
container2 = list()
for i in index_week:
    tmp = df2[(df2["Appt Date"] <= i) &(df2["Appt Date"] >i-1)] 
    container2.append(tmp["source"].value_counts().to_frame(i))
result2 = pd.concat(container2, axis=1).fillna(0)
