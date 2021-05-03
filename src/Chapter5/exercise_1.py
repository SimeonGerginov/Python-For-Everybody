# Exercise 5.1: Write a program which repeatedly reads numbers until the
# user enters “done”. Once “done” is entered, print out the total, count,
# and average of the numbers. If the user enters anything other than a
# number, detect their mistake using try and except and print an error
# message and skip to the next number.

# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.333333333333333

# Python for Everybody: Exploring Data Using Python 3
# by Charles R. Severance

total = 0.0
count = 0
average = 0.0

while True:
    input_number = input("Enter a number: ")
    if input_number == "done":
        break

    number = None
    try:
        number = float(input_number)
    except:
        print("Invalid input")
        continue

    total += number
    count += 1

average = total / count

print(total, count, average)
