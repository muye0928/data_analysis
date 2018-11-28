"""this task is to count how many customers came from each channel monthly and how many bookings came from each channel monthly"""
import pandas as pd
# step 1 load registration data
df = pd.read_csv("registration.csv")
df = df[["Date", "full name", "Source"]]
df["Date"] = pd.to_datetime(df["Date"])
df["year-month"] = df["Date"].apply(lambda x: str(x.year) +"-"+ str(x.month))

# step 2 data cleaning for source data --text
origin = df["Source"].values
df["Source"] = [i.replace(" ", "").lower() if type(i) == str else None for i in origin] # delete space and make them become lower characters
df = df.dropna()
# drop data in source including "x","ad","no", and other florin signs
# replace fb and ig
df = df[~df['Source'].isin(["x"])]
df = df[~df['Source'].isin(["ad"])]
df = df.replace("fb", "facebook")
df = df.replace("ig","instagram")
df['Source'] = df['Source'].str.replace('[^\w\s]','')
df=df[~df['Source'].isin(["no"])]

def ins(x):
    if "ins" in x:
        return "instagram"
    if "gram" in x:
        return "instagram"
    if "ig" in x:
        return "instagram"
    else:
        return x


def fb(x):
    if "fb" in x:
        return "facebook"
    if "book" in x:
        return "facebook"
    if "social" in x:
        return "facebook"
    else:
        return x


def friend(x):
    if "friend" in x:
        return "friend"
    if "refer" in x:
        return "friend"
    if "rf" in x:
        return "friend"
    if "daughter" in x:
        return "friend"
    if "cousin" in x:
        return "friend"
    if "family" in x:
        return "friend"
    if "sister" in x:
        return "friend"
    if "wife" in x:
        return "friend"
    if "husband" in x:
        return "friend"
    if "gf" in x:
        return "friend"
    if "told" in x:
        return "friend"
    if "coworker" in x:
        return "friend"
    if "fried" in x:
        return "friend"
    if "roommate" in x:
        return "friend"
    else:
        return x


def apple(x):
    if "app" in x:
        return "apple"
    else:
        return x


def yelp(x):
    if "yel" in x:
        return "yelp"
    if "review" in x:
        return "yelp"
    else:
        return x


def website(x):
    if "web" in x:
        return "website"
    if "online" in x:
        return "website"
    if "search" in x:
        return "website"
    if "snailz" in x:
        return "website"
    if "internet" in x:
        return "website"
    else:
        return x


def salon(x):
    if "sal" in x:
        return "salon"
    if "street" in x:
        return "salon"
    if "nail" in x:
        return "salon"
    if "walk" in x:
        return "salon"
    if "sign" in x:
        return "salon"
    if "flyer" in x:
        return "salon"
    if "shop" in x:
        return "salon"
    if "window" in x:
        return "salon"
    else:
        return x


def google(x):
    if "goog" in x:
        return "google"
    else:
        return x


def pinterest(x):
    if "pint" in x:
        return "pinterest"
    else:
        return x


def event(x):
    if "event" in x:
        return "event"
    if "cew" in x:
        return "event"
    if "wework" in x:
        return "event"
    else:
        return x

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

# step3 load bookings data
df2 = pd.read_csv("bookings1126.csv")
df2 = df2[["Full Name","Appt Date",'Referral Code','Snailz Discount Code',"Status"]]
df2["Appt Date"] = pd.to_datetime(df2["Appt Date"])
df2 = df2[df2["Status"] == "done"]
df2["year-month"] = df2["Appt Date"].apply(lambda x: str(x.year) +"-"+ str(x.month))

# step 4 find the unique name from each channel

#find unique name which source are friends and those who using referral code
refer = df2.dropna(subset = ["Referral Code"])
source_friend = df[df["Source"] == "friend"]
refername = refer["Full Name"].append(source_friend["full name"])
refername = set(refername)

#find unique name which source are website and those who using web code
webcode = df2[df2["Snailz Discount Code"] =="web10"].drop_duplicates(subset = "Full Name")
source_web = df[df["Source"] == "website"]
c = webcode["Full Name"]. append(source_web["full name"])
c = set(c)

# step 5 count how many people registrated from this channel monthly
# using facebook as an example
sour_fb = df[df["Source"] == "facebook"]
refb = sour_fb[["full name", "year-month"]]
refb.columns = ["full name", "ym"]
refb = refb.groupby("ym").count()
refb

# step 6 to find each booking came from which channel
source_ins = df[df["Source"] == "instagram"]
insname = set(source_ins["full name"])
df2["ins"] = df2.apply(lambda x :True if x["Full Name"] in insname else False,axis = 1)

source_goog = df[df["Source"] == "google"]
googlename = set(source_goog["full name"])
df2["goog"] = df2.apply(lambda x :True if x["Full Name"] in googlename else False,axis = 1)

source_yelp = df[df["Source"] == "yelp"]
yelpname = set(source_yelp["full name"])
df2["yelp"] = df2.apply(lambda x :True if x["Full Name"] in yelpname else False,axis = 1)

source_fb = df[df["Source"] == "facebook"]
fbname = set(source_fb["full name"])
df2["fb"] = df2.apply(lambda x :True if x["Full Name"] in fbname else False,axis = 1)

df2["friend"] = df2.apply(lambda x :True if x["Full Name"] in refername else False,axis = 1)

source_twitter = df[df["Source"] == "twitter"]
twname = set(source_twitter["full name"])
df2["tw"] = df2.apply(lambda x :True if x["Full Name"] in twname else False,axis = 1)

source_pint = df[df["Source"] == "pinterest"]
pintname = set(source_pint["full name"])
df2["pint"] = df2.apply(lambda x :True if x["Full Name"] in pintname else False,axis = 1)

source_app = df[df["Source"] == "apple"]
appname = set(source_app["full name"])
df2["app"] = df2.apply(lambda x :True if x["Full Name"] in appname else False,axis = 1)

source_salon = df[df["Source"] == "salon"]
salonname = set(source_salon["full name"])
df2["salon"] = df2.apply(lambda x :True if x["Full Name"] in salonname else False,axis = 1)

source_website = df[df["Source"] == "website"]
websitename = set(source_website["full name"])
df2["website"] = df2.apply(lambda x :True if x["Full Name"] in websitename else False,axis = 1)

source_event = df[df["Source"] == "event"]
eventname = set(source_event["full name"])
df2["event"] = df2.apply(lambda x :True if x["Full Name"] in eventname else False,axis = 1)

# step7 to count the bookings per channel monthly
year_month = df2["year-month"].unique()
result_ym = []
inst = []
google = []
yelp = []
facebook = []
twitter = []
pint = []
appl = []
frie = []
salon = []
website = []
event = []
for ym in year_month:
    result_ym.append(ym)
    tmp = df2[df2["year-month"] == ym]
    # instragram_count
    inst.append(len(tmp[(tmp["ins"] == True)]))
    # google_count
    google.append(len(tmp[(tmp["goog"] == True)]))
    # yelp_count
    yelp.append(len(tmp[(tmp["yelp"] == True)]))
    # facebook_count
    facebook.append(len(tmp[(tmp["fb"] == True)]))
    # twitter_count
    twitter.append(len(tmp[(tmp["tw"] == True)]))
    # pinterest_count
    pint.append(len(tmp[tmp["pint"] == True]))
    # app_count
    appl.append(len(tmp[tmp["app"] == True]))
    # friend_count
    frie.append(len(tmp[tmp["friend"] == True]))
    # salon_count
    salon.append(len(tmp[tmp["salon"] == True]))
    # website
    website.append(len(tmp[tmp["website"] == True]))
    # event
    event.append(len(tmp[tmp["event"] == True]))

result = pd.DataFrame({"year-month": result_ym, "ins": inst, "google": google, "yelp": yelp,
                       "facebook": facebook, "twitter": twitter,
                       "pinterest": pint, "apple": appl, "friend": frie, "salon": salon,
                       "website": website, "event": event})
result