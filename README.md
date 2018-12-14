# operation data analysis

### [channel analysis](https://github.com/muye0928/data_analysis/blob/master/channel_analysis.py)
- customer acquision cost
- booking acquision cost

·# to determine each bookings' source
df2.loc[:,'source'] = 'yyy'
source = ["instagram", "google","yelp","facebook","apple","salon","pinterest","event","twitter","website","friend"]
for item in source:
    source_a = df[df["Source"] == item]
    tmp = set(source_a["full name"])
    df2["source"] = df2.apply(lambda x: item if x["Full Name"] in tmp else x["source"],axis=1)·

### customer analysis
- [unique customers](https://github.com/muye0928/data_analysis/blob/master/unique_customers.py)
- [unique repeat customers](https://github.com/muye0928/data_analysis/blob/master/unique_customers.py)
- [average customer spending](https://github.com/muye0928/data_analysis/blob/master/average_customers_spending.py)
- [active customers](https://github.com/muye0928/data_analysis/blob/master/active_customers.py)
- focus groups
- coherent anaylsis
### coupon analysis
- [track coupon performance (based on one month and two months)](https://github.com/muye0928/data_analysis/blob/master/track_coupoun.py)
- [track coupon unique cumulative repeat bookings](https://github.com/muye0928/data_analysis/blob/master/track%20uniqe%20repeat%20bookings.py)
- [free services performance](https://github.com/muye0928/data_analysis/blob/master/free_serive_performance.py)
### data visualization
- [customer heatmap](https://github.com/muye0928/data_analysis/blob/master/heatmap.py) (using python and Tableau)
![](https://github.com/muye0928/data_analysis/blob/master/heatmap.PNG?raw=true)
![](https://img3.doubanio.com/view/photo/l/public/p2542626383.jpg)
