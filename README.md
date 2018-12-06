# some tasks for operations analysis based on registration data and bookings data

## 1. channel analysis
this task is to determine each registration record' source and each bookings source.Then, we need to count how many people from each channel(source) monthly and weekly.

## 2. create heatmap based on zip codes
this tasks used zipcode from registration data
I used python folium to create heatmap
I also used Tableau to create heatmap which is more efficient.

## 3. free services performance
this task is to measure the free services performance, to find how many people came back and completed bookings and 
how many people came back no matter their bookings status

## 4. track promotion code performance 
this task is to track how many people come back(cumulative repeat bookings) after using different codes monthly
and how many people came back based on 2-month code-users and how many people came back based on this month code-users

## 5. count active customers monthly 
 we define active customers are those in registration tab and still subscribed and at least completed bookings once
 
## 6. unique customers
we count unique customers in the specific period by drop duplicate record( subset = ID)
we define unique repeat customers are unique customers and booked more than once

## 7. active booked customers
we define active booked customers are customers who registrated and subscribed and booked at least once.
