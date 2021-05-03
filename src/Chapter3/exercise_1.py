# Exercise 3.1: Rewrite your pay computation to give the employee 1.5 times the
# rate for hours worked above 40 hours.

# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

# Python for Everybody: Exploring Data Using Python 3
# by Charles R. Severance

hours = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))

additional_hours = hours - 40
gross_pay = 0

if additional_hours > 0:
    hours_with_rate_per_hour = hours - additional_hours
    gross_pay = hours_with_rate_per_hour * rate_per_hour

    modified_rate_per_hour = rate_per_hour * 1.5
    gross_pay += additional_hours * modified_rate_per_hour
else:
    gross_pay = hours * rate_per_hour

print(gross_pay)
