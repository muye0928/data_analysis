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
df2 = pd.read_csv("bookings.csv")
df2["Full Name"] = df2["First Name"] +" " +df2["Last Name"]
df2 = df2[["Full Name","Appt Date",'Referral Code','Snailz Discount Code',"Status"]]
df2["Appt Date"] = pd.to_datetime(df2["Appt Date"])
df2 = df2[df2["Status"] == "done"]

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

onemonth = df[df["year-month"] =="2018-11"].drop_duplicates(subset = "full name")
onemonth["full name"].isin(webname).value_counts()
onemonth["full name"].isin(refername).value_counts()

#count weekly registration data
df['Week/Year'] = df['Date'].apply(lambda x: "%d/%d" % (x.week, x.year))
sour_fb = df[df["Source"] == "facebook"]
refb = sour_fb[["full name", "Week/Year"]]
refb.columns = ["full name", "ym"]
refb = refb.groupby("ym").count()
refb

# to determine each bookings' source
df2["source"] = df2.apply(lambda x :"friend" if x["Full Name"] in refername else "0",axis = 1)
df2["source"] = df2.apply(lambda x :"website" if x["Full Name"] in webname else x["source"] ,axis = 1)
source = ["instagram", "google","yelp","facebook","apple","salon","pinterest","event","twitter"]
for item in source:
    source_a = df[df["Source"] == item]
    tmp = set(source_a["full name"])
    df2["source"] = df2.apply(lambda x: item if x["Full Name"] in tmp else x["source"],axis=1)
    
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
