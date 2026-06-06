
# PART 1 - USER INPUT
city = input("enter your city name:")
temp= float(input("enter today's temperature in c:"))



# PART 2 if STATMENT
if temp > 35:
    print("warning: it is very hot today!")


# PART 3 - if-else
if temp > 25:
     print("great day to go outside!")
else:
     print("grab a jacket before you go out!")


# PART 4 if-elif-else
if temp > 35:
     print("weather: scorching hot")
elif temp > 25:
     print("weather: warm and sunny")
elif temp > 15:
     print("weather: cool and breezy")
else:
     print("weather: cold - stay warm")
     

# PART 5 - datetime MODULE
import datetime
import calendar

now = datetime.datetime.now()
print("city:", city)
print("time now:", now)

print(calendar.calendar(now.year))