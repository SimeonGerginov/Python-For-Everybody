# Exercise 3.2: Rewrite your pay program using try and except so that your
# program handles non-numeric input gracefully by printing a message
# and exiting the program. The following shows two executions of the
# program:

# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input

# Enter Hours: forty
# Error, please enter numeric input

# Python for Everybody: Exploring Data Using Python 3
# by Charles R. Severance

hours = 0.0
rate_per_hour = 0.0

try:
    hours = float(input("Enter hours: "))
    rate_per_hour = float(input("Enter rate per hour: "))
except:
    print("Error, please enter numeric input")
    quit()

additional_hours = hours - 40.0
gross_pay = 0.0

if additional_hours > 0.0:
    hours_with_rate_per_hour = hours - additional_hours
    gross_pay = hours_with_rate_per_hour * rate_per_hour

    modified_rate_per_hour = rate_per_hour * 1.5
    gross_pay += additional_hours * modified_rate_per_hour
else:
    gross_pay = hours * rate_per_hour

print(gross_pay)
