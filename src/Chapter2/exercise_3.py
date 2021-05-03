# Exercise 2.3: Write a program to prompt the user for hours and rate per
# hour to compute gross pay.

# Enter Hours: 35
# Enter Rate: 2.75
# Pay: 96.25

# We won’t worry about making sure our pay has exactly two digits after the decimal
# place for now. If you want, you can play with the built-in Python round function
# to properly round the resulting pay to two decimal places.

# Python for Everybody: Exploring Data Using Python 3
# by Charles R. Severance

hours = float(input("Enter Hours: "))
rate_per_hour = float(input("Enter Rate: "))

gross_pay = hours * rate_per_hour
print("Pay:", round(gross_pay, 2))
