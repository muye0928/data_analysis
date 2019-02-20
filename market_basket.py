import pandas as pd
#load data
df = pd.read_csv("bookings.csv")
# make sure those are completed bookings
df = df[df["Status"] =="done"]
# split the services bought together
services = df["Service"].str.split(',', expand=True)
services.columns = ['services1', 'services2',"services3","services4","services5"]
services = services[services.services2.notnull()] # filter nan value in second services column
results = services.groupby(["services1", "services2"]).size() # find duplicated services name and the count number
results = results.to_frame()

# for three services
service3 = services[services.services3.notnull()]
results3 = service3.groupby(["services1", "services2","services3"]).size()