# Exercise 4.6: Rewrite your pay computation with time-and-a-half for overtime and
# create a function called computepay which takes two parameters (hours and rate).

# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

# Python for Everybody: Exploring Data Using Python 3
# by Charles R. Severance

def computepay(hours, rate) :
    additional_hours = hours - 40.0
    gross_pay = 0.0

    if additional_hours > 0.0:
        hours_with_rate_per_hour = hours - additional_hours
        gross_pay = hours_with_rate_per_hour * rate

        modified_rate_per_hour = rate * 1.5
        gross_pay += additional_hours * modified_rate_per_hour
    else :
        gross_pay = hours * rate

    return gross_pay

hours = 0.0
rate_per_hour = 0.0

try :
    hours = float(input("Enter hours: "))
    rate_per_hour = float(input("Enter rate per hour: "))
except :
    print("Error, please enter numeric input")
    quit()

gross_pay = computepay(hours, rate_per_hour)

print("Pay", gross_pay)
