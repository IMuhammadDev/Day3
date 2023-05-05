# 4 ga teng bo'linadigan har yili
# ** bundan mustasno** har yili 100 ga teng bo'linadigan
# **agar** yil ham 400 ga teng bo‘linmasa

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

if year % 4 == 0:
    if year % 100 != 0 & year % 400 == 0:
        print("Leap year.")
    else:
        print("Not leap year.")

else:
    print("Not leap year.")
# Write your code below this line 👇
